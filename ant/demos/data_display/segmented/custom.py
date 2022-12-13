import reflect as r
import reflect_antd as antd
import reflect_html as html
import reflect_ant_icons as ant_icons


def app():
    first = antd.Segmented(
        options=[
            {
                "label": html.div(
                    [
                        antd.Avatar(src="https://joeschmoe.io/api/v1/random"),
                        html.div("User 1"),
                    ],
                    style={"padding": 4},
                ),
                "value": "user1",
            },
            {
                "label": html.div(
                    [
                        antd.Avatar(style={"backgroundColor": "#f56a00"}),
                        html.div("User 2"),
                    ],
                    style={"padding": 4},
                ),
                "value": "user2",
            },
            {
                "label": html.div(
                    [
                        antd.Avatar(
                            style={"backgroundColor": "87d068"},
                            icon=ant_icons.UserOutlined(),
                        ),
                        html.div("User 3"),
                    ],
                    style={"padding": 4},
                ),
                "value": "user3",
            },
        ]
    )
    second = antd.Segmented(
        options=[
            {
                "label": html.div(
                    [
                        html.div("Spring"),
                        html.div("Jan-Mar"),
                    ],
                    style={"padding": 4},
                ),
                "value": "spring",
            },
            {
                "label": html.div(
                    [
                        html.div("Summer"),
                        html.div("Apr-Jun"),
                    ],
                    style={"padding": 4},
                ),
                "value": "summer",
            },
            {
                "label": html.div(
                    [
                        html.div("Autumn"),
                        html.div("Jul-Sep"),
                    ],
                    style={"padding": 4},
                ),
                "value": "autumn",
            },
            {
                "label": html.div(
                    [
                        html.div("Winter"),
                        html.div("Oct-dec"),
                    ],
                    style={"padding": 4},
                ),
                "value": "winter",
            },
        ]
    )


    result = html.div([first, html.br(), second])
    r.autoprint(first)
    return result
