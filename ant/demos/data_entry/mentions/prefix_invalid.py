from reflect_html import *
from reflect_antd import Mentions
Option = Mentions.Option
prefix = this.prefix
def app():
    return Mentions([""{(MOCK_DATA[prefix] || []).map(valulambda e:(", Option(""{value}"", key=value, value=value), "))}""], style=dict(width='100%'), placeholder="input @ to mention people, # to mention tag", prefix=['@', '#'], onSearch=this.onSearch)
def app():
    return App()