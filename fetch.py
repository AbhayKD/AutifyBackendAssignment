import os
import sys
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import argparse

HOME = os.path.expanduser('~')
CWD = os.getcwd()

def save_page(url, pagefilename='page'):
    try:
        session = requests.Session()
        response = session.get(url)
        soup = BeautifulSoup(response.text)
        filename = url.replace("http://", "").replace("https://", "")
        with open(f'{filename}.html', 'w') as file:
            file.write(soup.prettify())
    except Exception as exception:
        print(f'Error-------- {exception}')

def get_metadata():
    pass


def main():
    parser = argparse.ArgumentParser(
        description='Utility to download web pages given a list of web urls')
    parser.add_argument('urls', metavar='URLs', type=str,
                        nargs='+', help='list of urls')
    parser.add_argument('--metadata', action='store_true',
                        default=False, help='get metadata')
    args = parser.parse_args()

    if (len(args.urls) > 0):
        for url in args.urls:
            save_page(url)
    else:
        print("No urls found from the input")


if __name__ == "__main__":
    main()
