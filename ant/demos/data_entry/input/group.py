import reflect_antd as antd
import reflect_html as html

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
                    antd.Input(style={"width": "20%"}, defaultValue="0571"),
                    antd.Input(style={"width": "30%"}, defaultValue="26888888"),
                ],
                compact=True,
            ),
            html.br(),
            antd.Input.Group(
                [
                    antd.Select(
                        options=[
                            {"label": "Zhejiang", "value": "Zhejiang"},
                            {"label": "Jiangsu", "value": "Jiangsu"},
                        ],
                        defaultValue="Zhejiang",
                    ),
                    antd.Input(
                        style={"width": "50%"}, defaultValue="Xihu District, Hangzhou"
                    ),
                ],
                compact=True,
            ),
            html.br(),
            antd.Input.Group(
                [
                    antd.Input.Search(style={"width": "40%"}, defaultValue="0571"),
                    antd.Input.Search(
                        allowClear=True, style={"width": "40%"}, defaultValue="26888888"
                    ),
                ],
                compact=True,
            ),
            html.br(),
            antd.Input.Group(
                [
                    antd.Input.Search(
                        allowClear=True, style={"width": "40%"}, defaultValue="0571"
                    ),
                    antd.Input.Search(
                        allowClear=True, style={"width": "40%"}, defaultValue="26888888"
                    ),
                ],
                compact=True,
            ),
            html.br(),
            antd.Input.Group(
                [
                    antd.Select(
                        options=[
                            {"label": "Option1", "value": "Option1"},
                            {"label": "Option2", "value": "Option2"},
                        ],
                        defaultValue="Option1",
                    ),
                    antd.Input(style={"width": "50%"}, defaultValue="input content"),
                    antd.InputNumber(),
                ],
                compact=True,
            ),
            html.br(),
            antd.Input.Group(
                [
                    antd.Input(style={"width": "50%"}, defaultValue="input content"),
                    antd.DatePicker(style={"width": "50%"}),
                ],
                compact=True,
            ),
            html.br(),
            antd.Input.Group(
                [
                    antd.Input(style={"width": "30%"}, defaultValue="input content"),
                    antd.DatePicker.RangePicker(style={"width": "70%"}),
                ],
                compact=True,
            ),
            html.br(),
            antd.Input.Group(
                [
                    antd.Select(
                        options=[
                            {"label": "Option1-1", "value": "Option1-1"},
                            {"label": "Option1-2", "value": "Option1-2"},
                        ],
                        defaultValue="Option1-1",
                    ),
                    antd.Select(
                        options=[
                            {"label": "Option2-1", "value": "Option2-1"},
                            {"label": "Option2-2", "value": "Option2-2"},
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
                        options=[
                            {"label": "Between", "value": "1"},
                            {"label": "Except", "value": "2"},
                        ],
                        defaultValue="1",
                    ),
                    antd.Input(
                        style={"width": 100, "textAlign": "center"},
                        placeholder="Minimum",
                    ),
                    antd.Input(
                        className="site-input-split",
                        style={
                            "width": 30,
                            "borderLeft": 0,
                            "borderRight": 0,
                            "pointerEvents": "none",
                        },
                        placeholder="~",
                        disabled=True,
                    ),
                    antd.Input(
                        className="site-input-right",
                        style={"width": 100, "textAlign": "center"},
                        placeholder="Maximum",
                    ),
                ],
                compact=True,
            ),
            html.br(),
            antd.Input.Group(
                [
                    antd.Select(
                        options=[
                            {"label": "Sign Up", "value": "Sign Up"},
                            {"label": "Sign In", "value": "Sign In"},
                        ],
                        defaultValue="Sign Up",
                        style={"width": "30%"},
                    ),
                    antd.AutoComplete(
                        style={"width": "70%"},
                        placeholder="Email",
                        options=[{"value": "text 1"}, {"value": "text 2"}],
                        compact=True,
                    ),
                    html.br(),
                    antd.Input.Group(
                        [
                            antd.Select(
                                options=[
                                    {"label": "Home", "value": "Home"},
                                    {"label": "Company", "value": "Company"},
                                ],
                                style={"width": "30%"},
                                defaultValue="Home",
                            ),
                            antd.Cascader(
                                style={"width": "70%"},
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
