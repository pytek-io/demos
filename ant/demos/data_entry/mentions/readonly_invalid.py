from render_antd import Mentions
from render_html import *

Option = Mentions.Option
def app(_):
    return[
 div(Mentions(""{getOptions()}"", style=dict(width='100%'), placeholder="this is disabled Mentions", disabled=True), style=dict(marginBottom=10)),
 Mentions(""{getOptions()}"", style=dict(width='100%'), placeholder="this is readOnly Mentions", readOnly=True),
]
def app(_):
    return App()