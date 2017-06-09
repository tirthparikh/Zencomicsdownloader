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

# Getting the file path and creating necessary directories
folder_path = sys.argv[1]
if folder_path is None:
    folder_path = os.getcwd()
    logging.info("No path entered,saving it to the current directory.")
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
os.chdir(folder_path)
os.mkdir("Zen Pencils Comics")
logging.info("Directory \"Zen Pencils Comics\" created")



# -----------------------------
#        Tasks to perform
# -----------------------------
# 1. Load the Home page
# 2. Saves the Comic image on that page
# 3. Follow the previous comic links
# 4. Repeat Untill it reaches the first comic
