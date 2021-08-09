import os
import json
from utils.enums import MetaFileName
from json.decoder import JSONDecodeError


def run(url):
    filepath = f'./{MetaFileName}'
    try:
        with open(filepath, 'r') as readfile:
            # read the meta file.
            meta_json = json.load(readfile)
            # update the meta file data.
            if url in meta_json:
                metadata = meta_json[url]
                if(type(metadata) is dict):
                    print(
                        f'''site: {metadata['site']}\nnum_links: {metadata['links_count']}\nimages: {metadata['img_count']}\nlast_fetch: {metadata['last_fetch']}\n'''
                    )
                else:
                    print(f'No meta data found for {url}\n')
            else:
                print(f'No meta data found for {url}\n')
            readfile.close()
    except (OSError, JSONDecodeError):
        print(f'No meta data found for {url}\n')
