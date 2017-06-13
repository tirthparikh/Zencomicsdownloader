import sys
from Downloader import ZenComicsDownloader as zcd

if __name__ == "__main__":
    try:
        zcd.main(sys.argv[1])
    except IndexError as e:
        zcd.main("")
