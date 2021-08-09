import json

from utils.enums import MetaFileName
from json.decoder import JSONDecodeError


def get_filename(url):
    return url.replace("http://", "").replace("https://", "").replace("/", "\\")


def update_metainfo(metadata):
    filepath = f'./{MetaFileName}'
    site_name = metadata['site']
    meta_json = {}
    try:
        with open(filepath, 'r') as readfile:
            # read the meta file.
            meta_json = json.load(readfile)
            # update the meta file data.
            meta_json[site_name] = metadata
            readfile.close()
    except (OSError, JSONDecodeError):
        meta_json[site_name] = metadata
    with open(filepath, 'w') as writefile:
        # write the meta file
        json.dump(meta_json, writefile)
        writefile.close()


# def get_url_folder_path(url):
#     folder_name = url.replace("http://", "").replace("https://", "")
#     page_folder_path = f'{HOME}/fetch/{folder_name}'
#     if not os.path.exists(page_folder_path):
#         os.makedirs(page_folder_path, exist_ok=True)
#     return page_folder_path