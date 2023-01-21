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
                buttonStyle="solid",
            ),
            antd.Radio.Group(
                [
                    antd.Radio.Button("Hangzhou", value="a"),
                    antd.Radio.Button("Shanghai", value="b", disabled=True),
                    antd.Radio.Button("Beijing", value="c"),
                    antd.Radio.Button("Chengdu", value="d"),
                ],
                defaultValue="c",
                buttonStyle="solid",
                style={"marginTop": 16},
            ),
        ]
    )
