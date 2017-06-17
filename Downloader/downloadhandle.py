"""This module contains the functions needed to download files and
check if proper response is received from a url"""

import requests
from tqdm import tqdm
from progress.bar import ChargingBar


def check_connection(url, stream=False):
    """checks if the connection is made and returns the response"""
    try:
        res = requests.get(url, stream=stream)
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
    return (False, error)


def download_image(image_link):
    connected, response = check_connection(image_link, stream=True)
    if not connected:
        return False

    filename = image_link.rsplit("/", 1)[1]
    max_ = int(response.headers["Content-Length"])/100000
    bar = ChargingBar("Downloading", max=max_, suffix='%(percent)d%%')
    with open(filename, "wb") as f:
        for chunk in response.iter_content(100000):
            f.write(chunk)
            bar.next()
        bar.finish()


    return True
