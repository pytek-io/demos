from reflect_html import *
from reflect_antd import Tag


def app():
    return [
        Tag("Twitter", icon=TwitterOutlined([]), color="#55acee"),
        Tag("Youtube", icon=YoutubeOutlined([]), color="#cd201f"),
        Tag("Facebook", icon=FacebookOutlined([]), color="#3b5999"),
        Tag("LinkedIn", icon=LinkedinOutlined([]), color="#55acee"),
    ]
