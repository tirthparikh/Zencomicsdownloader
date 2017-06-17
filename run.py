#! /usr/bin/env python3

import sys
import Downloader.ZenComicsDownloader as zcd

if __name__ == "__main__":
    try:
        zcd.main(sys.argv[1])
    except IndexError as e:
        zcd.main("")
