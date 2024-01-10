from render_antd import Select, Spin
from render_html import *

Option = Select.Option
fetching, data, value = this.fetching, this.data, this.value
def app(_):
    return[
 Select(mode="multiple", labelInValue=True, value=value, placeholder="Select users", notFoundContent="{fetching ? <Spin size=", small"=True),
 Option(""{d.text}"", key=d.value),
]
def app(_):
    return UserRemoteSelect()