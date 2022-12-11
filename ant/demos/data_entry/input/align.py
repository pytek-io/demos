import reflect_antd as antd
import reflect_html as html

Text = antd.Typography.Text
RangePicker = antd.DatePicker.RangePicker
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
narrowStyle = {"width": 50}


def app():
    return html.div(
        [
            antd.Mentions(style=dict(width=100)),
            antd.Input.TextArea(rows=1, style=dict(width=100)),
            antd.Button("Button", type="primary"),
            antd.Input(style=dict(width=100)),
            Text("Ant Design", copyable=True),
            antd.Input(prefix="1", suffix="2", style=dict(width=100)),
            antd.Input(addonBefore="1", addonAfter="2", style=dict(width=100)),
            antd.InputNumber(style=dict(width=100)),
            antd.DatePicker(style=dict(width=100)),
            antd.TimePicker(style=dict(width=100)),
            antd.Select(
                options=[
                    {"label": "Jack", "value": "jack"},
                    {"label": "Lucy", "value": "lucy"},
                    {"label": "Disabled", "value": "disabled", "disabled": True},
                    {"label": "yiminghe", "value": "Yiminghe"},
                ],
                style=dict(width=100),
                defaultValue="jack",
            ),
            antd.TreeSelect(style=dict(width=100)),
            antd.Cascader(
                defaultValue=["zhejiang", "hangzhou", "xihu"], options=options
            ),
            RangePicker(),
            antd.DatePicker(picker="month"),
            antd.Radio.Group(
                [
                    antd.Radio.Button("Hangzhou", value="a"),
                    antd.Radio.Button("Shanghai", value="b"),
                ],
                defaultValue="a",
            ),
            antd.AutoComplete(style=dict(width=100), placeholder="input here"),
            html.br(),
            antd.Input(
                prefix="$",
                addonBefore="Http://",
                addonAfter=".com",
                defaultValue="mysite",
            ),
            antd.Input(style=narrowStyle, suffix="Y"),
            antd.Input(style=narrowStyle),
            antd.Input(style=narrowStyle, defaultValue="1", suffix="Y"),
        ]
    )
