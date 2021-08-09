import os
import sys
import argparse

from urllib.parse import urljoin
from handles import save_page, get_metadata



HOME = os.path.expanduser('~')
CWD = os.getcwd()

TAGS_TO_SAVE = {
    'img': {'inner': 'src'},
    'link': {'inner': 'href'},
    # 'script': {'inner': 'src'}
}


def soup_find_and_save(pagefolder, url, soup, session, tag2find, inner):
    for res in soup.findAll(tag2find):   # images, css, etc..
        try:
            if(res.get(inner)):
                fileurl = urljoin(url, res.get(inner))
                filename = os.path.basename(res[inner])
                # rename to saved file path
                # res[inner] # may or may not exist
                filepath = os.path.join(pagefolder, filename)
                res[inner] = os.path.join(
                    os.path.basename(pagefolder), filename)
                if not os.path.isfile(filepath):  # was not downloaded
                    with open(filepath, 'wb') as file:
                        filebin = session.get(fileurl)
                        file.write(filebin.content)
        except Exception as exception:
            print(exception)
    # return soup


def decide_perform_action(metadata, urls):
    for url in urls:
        if(metadata == True):
            get_metadata.run(url)
        else:
            save_page.run(url)

def main():
    parser = argparse.ArgumentParser(
        description='Utility to download web pages given a list of web urls')
    parser.add_argument('urls', metavar='URLs', type=str,
                        nargs='+', help='list of urls')
    parser.add_argument('--metadata', action='store_true',
                        default=False, help='get metadata')
    args = parser.parse_args()

    if (len(args.urls) > 0):
        decide_perform_action(**vars(args))
    else:
        print("No urls found from the input")


if __name__ == "__main__":
    main()
