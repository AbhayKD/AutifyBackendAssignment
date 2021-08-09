from enum import Enum

class Tags(Enum):
    IMG = 'img'
    LINK = 'link'
    SCRIPT = 'script'
    ANNOTATION = 'a'

class TagsInner(Enum):
    IMG = 'src'
    LINK = 'href'
    SCRIPT = 'href'
    ANNOTATION = 'href'

MetaDataTags = [Tags.IMG, Tags.LINK, Tags.ANNOTATION]
SaveTags = [Tags.IMG, Tags.LINK]
MetaFileName = '.web_dwnld_metadata.json'
