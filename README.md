# Content-Select Downloader

PDF-Downloader for content-select.com which bundles all chapters to one file.

## Installation with dependencies

Python 3 >= 3.6\
Chromium

**Install virtualenv**
```
pip install virtualenv
```

**Clone repository**
```
git clone https://github.com/adrblo/content-select-downloader csdownloader
cd csdownloader
```

**Create a virtual environment and activate it**
```
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Execution

**Configure environment variables**

Create a file named '.env' like the '.env.sample'-File in the repository.\
Set USER_DATA_DIR to your Chromium user data dir and PROFILE_DIR to your profile name (default: Default).
See `chrome://version/` in Chromium for "Profile Path" and separate the path.\
(e.g. `/home/<user>/.config/chromium/Default` with `/home/<user>/.config/chromium/` as user data directory and
`Default` as profile directory)

**Log in to Content-Select.com**

Open your Chromium browser and log in to content-select.com. You need to close the browser otherwise the script will fail.


**Run command**

```
> python cs_downloader.py --help
Usage: cs_downloader.py [OPTIONS] URL FILENAME

Arguments:
  URL       [required]
  FILENAME  [required]

Options:
  --help                          Show this message and exit.
```

The URL has to be something like `https://content-select.com/media/moz_viewer/<uuid>/language:de` and filename `book.pdf`:
```
python cs_downloader.py https://content-select.com/media/moz_viewer/<uuid>/language:de book.py
```


## Disclaimer

This software is just for scientific purposes and not a piracy tool. Every download needs a valid Account.
