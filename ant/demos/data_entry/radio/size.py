import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Radio.Group(
                [
                    antd.Radio.Button("Hangzhou", value="a"),
                    antd.Radio.Button("Shanghai", value="b"),
                    antd.Radio.Button("Beijing", value="c"),
                    antd.Radio.Button("Chengdu", value="d"),
                ],
                defaultValue="a",
                size="large",
            ),
            antd.Radio.Group(
                [
                    antd.Radio.Button("Hangzhou", value="a"),
                    antd.Radio.Button("Shanghai", value="b"),
                    antd.Radio.Button("Beijing", value="c"),
                    antd.Radio.Button("Chengdu", value="d"),
                ],
                defaultValue="a",
                style={"marginTop": 16},
            ),
            antd.Radio.Group(
                [
                    antd.Radio.Button("Hangzhou", value="a"),
                    antd.Radio.Button("Shanghai", value="b"),
                    antd.Radio.Button("Beijing", value="c"),
                    antd.Radio.Button("Chengdu", value="d"),
                ],
                defaultValue="a",
                size="small",
                style={"marginTop": 16},
            ),
        ]
    )
