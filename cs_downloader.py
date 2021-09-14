import os
import time
import uuid
import typer

from bs4 import BeautifulSoup
from selenium import webdriver
from PyPDF2 import PdfFileMerger
from pydantic import BaseSettings


class Settings(BaseSettings):
    USER_DATA_DIR: str
    PROFILE_DIR: str = 'Default'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Settings()


def main(url: str, filename: str):
    temp_path = os.path.join(os.getcwd(), 'temp', str(uuid.uuid4()))

    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=" + config.USER_DATA_DIR)
    options.add_argument("profile-directory=" + config.PROFILE_DIR)
    prefs = {"download.default_directory": temp_path}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    print_list = soup.find(id="printList").find('ul')

    chapter_links = []

    for li in print_list.find_all('li'):
        a_tag = li.find('a')
        chapter_links.append(a_tag.attrs['href'])

    if not os.path.exists('temp'):
        os.mkdir('temp')
    os.mkdir(temp_path)

    for cl in chapter_links:
        driver.get('https://content-select.com' + cl)

    time.sleep(5)

    merger = PdfFileMerger()

    files = sorted([os.path.join(temp_path, file) for file in os.listdir(temp_path)], key=lambda t: os.stat(t).st_mtime)

    for file in files:
        merger.append(file)

    merger.write(filename)
    merger.close()


if __name__ == "__main__":
    typer.run(main)
