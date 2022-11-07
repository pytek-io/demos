from reflect_html import *
from reflect_antd import (
    Typography,
    Button,
    Input,
    Select,
    Cascader,
    TreeSelect,
    DatePicker,
    TimePicker,
    InputNumber,
    Radio,
    AutoComplete,
    Mentions,
)

Text = Typography.Text
Option = Select.Option
RangePicker = DatePicker.RangePicker


options = [
    {
        "value": "zhejiang",
        "label": "Zhejiang",
        "children": [
            {
                "value": "hangzhou",
                "label": "Hangzhou",
                "children": [{"value": "xihu", "label": "West Lake"}],
            }
        ],
    },
    {
        "value": "jiangsu",
        "label": "Jiangsu",
        "children": [
            {
                "value": "nanjing",
                "label": "Nanjing",
                "children": [{"value": "zhonghuamen", "label": "Zhong Hua Men"}],
            }
        ],
    },
]

narrowStyle = {
    "width": 50,
}


def app():
    return div(
        [
            Mentions(style=dict(width=100), rows=1),
            Input.TextArea(rows=1, style=dict(width=100)),
            Button("Button", type="primary"),
            Input(style=dict(width=100)),
            Text("Ant Design", copyable=True),
            Input(prefix="1", suffix="2", style=dict(width=100)),
            Input(addonBefore="1", addonAfter="2", style=dict(width=100)),
            InputNumber(style=dict(width=100)),
            DatePicker(style=dict(width=100)),
            TimePicker(style=dict(width=100)),
            Select(
                [
                    Option("Jack", value="jack"),
                    Option("Lucy", value="lucy"),
                    Option("Disabled", value="disabled", disabled=True),
                    Option("yiminghe", value="Yiminghe"),
                ],
                style=dict(width=100),
                defaultValue="jack",
            ),
            TreeSelect(style=dict(width=100)),
            Cascader(defaultValue=["zhejiang", "hangzhou", "xihu"], options=options),
            RangePicker(),
            DatePicker(picker="month"),
            Radio.Group(
                [
                    Radio.Button("Hangzhou", value="a"),
                    Radio.Button("Shanghai", value="b"),
                ],
                defaultValue="a",
            ),
            AutoComplete(style=dict(width=100), placeholder="input here"),
            br(),
            Input(
                prefix="$",
                addonBefore="Http://",
                addonAfter=".com",
                defaultValue="mysite",
            ),
            Input(style=narrowStyle, suffix="Y"),
            Input(style=narrowStyle),
            Input(style=narrowStyle, defaultValue="1", suffix="Y"),
        ]
    )
