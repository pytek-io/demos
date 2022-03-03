from reflect_html import *
from reflect_antd import Tag
CheckableTag = Tag.CheckableTag
selectedTags = this.selectedTags
selectedTags = this.selectedTags
def app():
    return[
 span("Categories:", style=dict(marginRight=8)),
 CheckableTag(""{tag}"", key=tag, checked=selectedTags.indexOf(tag) > -1, onChange=checked => this.handleChange(tag, checked)),
]
def app():
    return HotTags()