from render_antd import Select
from render_html import *

Option = Select.Option
def app(_):
    return Select(""{children}"", mode="tags", style=dict(width='100%'), placeholder="Tags Mode", onChange=handleChange)