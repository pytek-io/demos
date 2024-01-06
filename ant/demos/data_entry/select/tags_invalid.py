from render_html import *
from render_antd import Select
Option = Select.Option
def app():
    return Select(""{children}"", mode="tags", style=dict(width='100%'), placeholder="Tags Mode", onChange=handleChange)