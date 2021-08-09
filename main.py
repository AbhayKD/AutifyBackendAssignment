import argparse

from urllib.parse import urljoin
from handles import save_page, get_metadata

# from pywebcopy import save_webpage

'''
This method is responsible for deciding which action to perform depending 
upon the arguments provided.
'''
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
    # parser.add_argument('--downloadfull', action='store_true',
    #                     default=False, help='get metadata')
    args = parser.parse_args()
    # save_webpage(url='https://www.google.com', project_folder='./', bypass_robots=True, zip_project_folder=True)
    if (len(args.urls) > 0):
        decide_perform_action(**vars(args))
    else:
        print("No urls found from the input")


if __name__ == "__main__":
    main()
