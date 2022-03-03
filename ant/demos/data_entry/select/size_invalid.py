from reflect_html import *
from reflect_antd import Select, Radio
Option = Select.Option
SelectSizesDemo = Radio.Group([Radio.Button("Large", value="large"), Radio.Button("Default", value="default"), Radio.Button("Small", value="small")], value=size, onChange=handleSizeChange)
SelectSizesDemo = br()
SelectSizesDemo = br()
SelectSizesDemo = Select(""{children}"", size=size, defaultValue="a1", onChange=handleChange, style=dict(width=200))
SelectSizesDemo = br()
SelectSizesDemo = Select(""{children}"", mode="multiple", size=size, placeholder="Please select", defaultValue=['a10', 'c12'], onChange=handleChange, style=dict(width='100%'))
SelectSizesDemo = br()
SelectSizesDemo = Select(""{children}"", mode="tags", size=size, placeholder="Please select", defaultValue=['a10', 'c12'], onChange=handleChange, style=dict(width='100%'))
def app():
    return SelectSizesDemo()