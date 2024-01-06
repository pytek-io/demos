from render_html import *
from render_antd import Select, Spin
Option = Select.Option
fetching, data, value = this.fetching, this.data, this.value
def app():
    return[
 Select(mode="multiple", labelInValue=True, value=value, placeholder="Select users", notFoundContent="{fetching ? <Spin size=", small"=True),
 Option(""{d.text}"", key=d.value),
]
def app():
    return UserRemoteSelect()