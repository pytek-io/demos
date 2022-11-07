import reflect_antd as antd
import reflect_html as html

Option = antd.Select.Option
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
    return html.div(
        [
            antd.Input.Group(
                antd.Row(
                    [
                        antd.Col(antd.Input(defaultValue="0571"), span=5),
                        antd.Col(antd.Input(defaultValue="26888888"), span=8),
                    ],
                    gutter=8,
                ),
                size="large",
            ),
            html.br(),
            antd.Input.Group(
                [
                    antd.Input(style=dict(width="20%"), defaultValue="0571"),
                    antd.Input(style=dict(width="30%"), defaultValue="26888888"),
                ],
                compact=True,
            ),
            html.br(),
            antd.Input.Group(
                [
                    antd.Select(
                        [
                            Option("Zhejiang", value="Zhejiang"),
                            Option("Jiangsu", value="Jiangsu"),
                        ],
                        defaultValue="Zhejiang",
                    ),
                    antd.Input(
                        style=dict(width="50%"), defaultValue="Xihu District, Hangzhou"
                    ),
                ],
                compact=True,
            ),
            html.br(),
            antd.Input.Group(
                [
                    antd.Input.Search(style=dict(width="40%"), defaultValue="0571"),
                    antd.Input.Search(
                        allowClear=True,
                        style=dict(width="40%"),
                        defaultValue="26888888",
                    ),
                ],
                compact=True,
            ),
            html.br(),
            antd.Input.Group(
                [
                    antd.Input.Search(
                        allowClear=True, style=dict(width="40%"), defaultValue="0571"
                    ),
                    antd.Input.Search(
                        allowClear=True,
                        style=dict(width="40%"),
                        defaultValue="26888888",
                    ),
                ],
                compact=True,
            ),
            html.br(),
            antd.Input.Group(
                [
                    antd.Select(
                        [
                            Option("Option1", value="Option1"),
                            Option("Option2", value="Option2"),
                        ],
                        defaultValue="Option1",
                    ),
                    antd.Input(style=dict(width="50%"), defaultValue="input content"),
                    antd.InputNumber(),
                ],
                compact=True,
            ),
            html.br(),
            antd.Input.Group(
                [
                    antd.Input(style=dict(width="50%"), defaultValue="input content"),
                    antd.DatePicker(style=dict(width="50%")),
                ],
                compact=True,
            ),
            html.br(),
            antd.Input.Group(
                [
                    antd.Input(style=dict(width="30%"), defaultValue="input content"),
                    antd.DatePicker.RangePicker(style=dict(width="70%")),
                ],
                compact=True,
            ),
            html.br(),
            antd.Input.Group(
                [
                    antd.Select(
                        [
                            Option("Option1-1", value="Option1-1"),
                            Option("Option1-2", value="Option1-2"),
                        ],
                        defaultValue="Option1-1",
                    ),
                    antd.Select(
                        [
                            Option("Option2-1", value="Option2-1"),
                            Option("Option2-2", value="Option2-2"),
                        ],
                        defaultValue="Option2-2",
                    ),
                ],
                compact=True,
            ),
            html.br(),
            antd.Input.Group(
                [
                    antd.Select(
                        [Option("Between", value="1"), Option("Except", value="2")],
                        defaultValue="1",
                    ),
                    antd.Input(
                        style=dict(width=100, textAlign="center"), placeholder="Minimum"
                    ),
                    antd.Input(
                        className="site-input-split",
                        style=dict(
                            width=30, borderLeft=0, borderRight=0, pointerEvents="none"
                        ),
                        placeholder="~",
                        disabled=True,
                    ),
                    antd.Input(
                        className="site-input-right",
                        style=dict(width=100, textAlign="center"),
                        placeholder="Maximum",
                    ),
                ],
                compact=True,
            ),
            html.br(),
            antd.Input.Group(
                [
                    antd.Select(
                        [
                            Option("Sign Up", value="Sign Up"),
                            Option("Sign In", value="Sign In"),
                        ],
                        defaultValue="Sign Up",
                        style=dict(width="30%"),
                    ),
                    antd.AutoComplete(
                        style=dict(width="70%"),
                        placeholder="Email",
                        options=[{"value": "text 1"}, {"value": "text 2"}],
                        compact=True,
                    ),
                    html.br(),
                    antd.Input.Group(
                        [
                            antd.Select(
                                [
                                    Option("Home", value="Home"),
                                    Option("Company", value="Company"),
                                ],
                                style=dict(width="30%"),
                                defaultValue="Home",
                            ),
                            antd.Cascader(
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
