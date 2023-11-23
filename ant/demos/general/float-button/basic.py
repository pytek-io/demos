import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.FloatButton(
                shape="circle", badge={"dot": "true"}, style={"right": 164}
            ),
            antd.FloatButton.Group(
                [
                    antd.FloatButton(
                        href="https://ant.design/index-cn",
                        tooltip=html.div("custom badge color"),
                        badge={"count": 5, "color": "blue"},
                    ),
                    antd.FloatButton(badge={"count": 5}),
                ],
                shape="circle",
                style={"right": 94},
            ),
            antd.FloatButton.Group(
                [
                    antd.FloatButton(badge={"count": 12}),
                    antd.FloatButton(badge={"count": 123, "overflowCount": 999}),
                    antd.FloatButton.BackTop(visibilityHeight=0),
                ],
                shape="circle",
            ),
        ]
    )
