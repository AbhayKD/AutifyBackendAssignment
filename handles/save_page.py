import requests
import datetime
import re

from bs4 import BeautifulSoup
from utils.helpers import get_filename, update_metainfo
from utils.enums import TagsInner, Tags, MetaDataTags, SaveTags, MetaFileName


def extract_metadata_info(url, soup):
    metadata = {
        'img_count': 0,
        'links_count': 0,
        'last_fetch': datetime.datetime.now().strftime('%a %b %d %Y %H:%M %z'),
        'site': url
    }
    for tag in MetaDataTags:
        for res in soup.findAll(tag.value):
            value = res.attrs.get(TagsInner[tag.name].value)
            if value == "" or value is None:
                continue
            else:
                if (tag == Tags.IMG):
                    metadata['img_count'] += 1
                elif (tag == Tags.LINK or tag == Tags.ANNOTATION):
                    metadata['links_count'] += 1
    return metadata


def run(url):
    try:
        session = requests.Session()
        response = session.get(url)
        soup = BeautifulSoup(response.text, features='lxml')
        # page_folder_path = get_url_folder_path(url)
        # images = soup.find_all('img', {'src':re.compile('.jpg')})
        filename = get_filename(url)
        metadata = extract_metadata_info(url, soup)
        with open(f'{filename}.html', 'w') as file:
            file.write(soup.prettify())
        update_metainfo(metadata)
        # for tag in TAGS_TO_SAVE:
        #     soup_find_and_save(
        #         page_folder_path, url, soup, session, tag, TAGS_TO_SAVE[tag]['inner'])
    except Exception as exception:
        print(str(exception))
