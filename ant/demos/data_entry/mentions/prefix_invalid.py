from render_antd import Mentions
from render_html import *

Option = Mentions.Option
prefix = this.prefix
def app(_):
    return Mentions([""{(MOCK_DATA[prefix] || []).map(valulambda e:(", Option(""{value}"", key=value, value=value), "))}""], style=dict(width='100%'), placeholder="input @ to mention people, # to mention tag", prefix=['@', '#'], onSearch=this.onSearch)
def app(_):
    return App()