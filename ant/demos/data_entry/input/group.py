from reflect_html import *
from reflect_antd import (
    Input,
    Col,
    Row,
    Select,
    InputNumber,
    DatePicker,
    AutoComplete,
    Cascader,
)

Option = Select.Option

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

def app():
    return div(
        [
            Input.Group(
                Row(
                    [
                        Col(Input(defaultValue="0571"), span=5),
                        Col(Input(defaultValue="26888888"), span=8),
                    ],
                    gutter=8,
                ),
                size="large",
            ),
            br(),
            Input.Group(
                [
                    Input(style=dict(width="20%"), defaultValue="0571"),
                    Input(style=dict(width="30%"), defaultValue="26888888"),
                ],
                compact=True,
            ),
            br(),
            Input.Group(
                [
                    Select(
                        [
                            Option("Zhejiang", value="Zhejiang"),
                            Option("Jiangsu", value="Jiangsu"),
                        ],
                        defaultValue="Zhejiang",
                    ),
                    Input(
                        style=dict(width="50%"), defaultValue="Xihu District, Hangzhou"
                    ),
                ],
                compact=True,
            ),
            br(),
            Input.Group(
                [
                    Input.Search(style=dict(width="40%"), defaultValue="0571"),
                    Input.Search(
                        allowClear=True,
                        style=dict(width="40%"),
                        defaultValue="26888888",
                    ),
                ],
                compact=True,
            ),
            br(),
            Input.Group(
                [
                    Input.Search(
                        allowClear=True, style=dict(width="40%"), defaultValue="0571"
                    ),
                    Input.Search(
                        allowClear=True,
                        style=dict(width="40%"),
                        defaultValue="26888888",
                    ),
                ],
                compact=True,
            ),
            br(),
            Input.Group(
                [
                    Select(
                        [
                            Option("Option1", value="Option1"),
                            Option("Option2", value="Option2"),
                        ],
                        defaultValue="Option1",
                    ),
                    Input(style=dict(width="50%"), defaultValue="input content"),
                    InputNumber(),
                ],
                compact=True,
            ),
            br(),
            Input.Group(
                [
                    Input(style=dict(width="50%"), defaultValue="input content"),
                    DatePicker(style=dict(width="50%")),
                ],
                compact=True,
            ),
            br(),
            Input.Group(
                [
                    Input(style=dict(width="30%"), defaultValue="input content"),
                    DatePicker.RangePicker(style=dict(width="70%")),
                ],
                compact=True,
            ),
            br(),
            Input.Group(
                [
                    Select(
                        [
                            Option("Option1-1", value="Option1-1"),
                            Option("Option1-2", value="Option1-2"),
                        ],
                        defaultValue="Option1-1",
                    ),
                    Select(
                        [
                            Option("Option2-1", value="Option2-1"),
                            Option("Option2-2", value="Option2-2"),
                        ],
                        defaultValue="Option2-2",
                    ),
                ],
                compact=True,
            ),
            br(),
            Input.Group(
                [
                    Select(
                        [Option("Between", value="1"), Option("Except", value="2")],
                        defaultValue="1",
                    ),
                    Input(
                        style=dict(width=100, textAlign="center"), placeholder="Minimum"
                    ),
                    Input(
                        className="site-input-split",
                        style=dict(
                            width=30, borderLeft=0, borderRight=0, pointerEvents="none"
                        ),
                        placeholder="~",
                        disabled=True,
                    ),
                    Input(
                        className="site-input-right",
                        style=dict(width=100, textAlign="center"),
                        placeholder="Maximum",
                    ),
                ],
                compact=True,
            ),
            br(),
            Input.Group(
                [
                    Select(
                        [
                            Option("Sign Up", value="Sign Up"),
                            Option("Sign In", value="Sign In"),
                        ],
                        defaultValue="Sign Up",
                        style=dict(width="30%"),
                    ),
                    AutoComplete(
                        style=dict(width="70%"),
                        placeholder="Email",
                        options=[{"value": "text 1"}, {"value": "text 2"}],
                        compact=True,
                    ),
                    br(),
                    Input.Group(
                        [
                            Select(
                                [
                                    Option("Home", value="Home"),
                                    Option("Company", value="Company"),
                                ],
                                style=dict(width="30%"),
                                defaultValue="Home",
                            ),
                            Cascader(
                                style=dict(width="70%"),
                                options=options,
                                placeholder="Select Address",
                            ),
                        ]
                    ),
                ],
                compact=True,
            ),
        ],
        className="site-input-group-wrapper",
    )
