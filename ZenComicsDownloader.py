#! /usr/bin/env python3

"""Downloads all the comics from ZenPencils.com

You can run this program directly from your terminal as
./ZenComicsDownloader path-to-folder

"""

import sys
import os
import logging

import bs4
import warnings

from downloadhandle import check_connection, download_image

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
logging.basicConfig(filename="ZenPencilsLog.txt", level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)


def get_comic(address):
    """This function downloads the comic image"""
    connected, response = check_connection(address)
    if not connected:
        return False
    soup = bs4.BeautifulSoup(response.text)
    comic_element = soup.select("#comic img")

    # Clean up the image link
    image_link = comic_element[0].get('src')
    image_link = image_link.replace("//cdn.", "http://")
    return download_image(image_link)


def create_directory(target):
    folder_path = target

    # If no destination mentioned, set it to current directory
    if not folder_path:
        folder_path = os.getcwd()
    folder_path += "/ZenPencilComics"

    # Create a directory "ZenpencilComics to download all the comics
    os.makedirs(folder_path, exist_ok=True)
    logging.info("Creating directory : " + folder_path)

    return folder_path


# Main program ...
def main(args):
    # Connecting to Zenpencils.com's home page
    logging.info("Connecting to zenpencils.com")
    connected, response = check_connection("http://www.zenpencils.com")
    if not connected:
        logging.error(response)
        print("An Error occurred!")
        print(response)
        sys.exit(1)

    # Connection Successful
    logging.info("Connection successful")

    # Fetching Target Directory from command line argument
    folder_path = create_directory(args)
    os.chdir(folder_path)

    soup = bs4.BeautifulSoup(response.text)
    not_downloaded = []  # list of not downloaded comics

    # The links of all the comics are in the homepage under class: "level-0"
    comic_links = set(soup.select('.level-0'))

    for link in comic_links:
        logging.info("Downloading : " + comic_name)
        print("Attempting to download :" + comic_name)

        address = link['value']
        comic_name = address[28:]

        status = get_comic(address)
        if not status:
            logging.info("Download failed :" + comic_name)
            not_downloaded.append(address)
            print("Download failed for " + comic_name)
            continue

        print(comic_name + " downloaded")

    if len(not_downloaded) > 0:
        print("This files are not downloaded")
        for l in not_downloaded:
            print(l[28:])
    logging.info("Download Complete")

    print("Done!!")


if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except IndexError as e:
        main("")
