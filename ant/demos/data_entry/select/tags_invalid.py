from reflect_html import *
from reflect_antd import Select
Option = Select.Option
def app():
    return Select(""{children}"", mode="tags", style=dict(width='100%'), placeholder="Tags Mode", onChange=handleChange)