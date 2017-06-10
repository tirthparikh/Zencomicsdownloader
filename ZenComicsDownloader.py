#! /usr/bin/env python3

"""Downloads all the comics from ZenPencils.com

You can run this program directly from your terminal as
./ZenComicsDownloader path-to-folder

"""

import sys
import os
import logging
import requests
import webbrowser

import bs4
import warnings

# Configuring warnings and Log files
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
logging.basicConfig(filename="ZenPencilsLog.txt", level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')


def check_connection(url):
    """checks if the connection is made and returns the response"""
    try:
        res = requests.get(url)
        res.raise_for_status()
        return (True, res)
    except requests.exceptions.MissingSchema as e:
        error = "Invalid URL "+url
    except requests.exceptions.HTTPError as e:
        error = "HTTPError :"+str(res.status_code)
    except requests.exceptions.Timeout as e:
        error = "Connection Timeout! Please retry."
    except requests.exceptions.TooManyRedirects as e:
        error = "Too Many Redirects! Please refresh check the URL"
    except requests.exceptions.ConnectionError as e:
        error = "Connection Error! PLease check you Connections"
    return (False,error)



def _check_path(folder_path):
    return os.path.exists(folder_path)


# -----------------------------
#        Tasks to perform
# -----------------------------
# 1. Load the Home page
# 2. Saves the Comic image on that page
# 3. Follow the previous comic links
# 4. Repeat Untill it reaches the first comic
