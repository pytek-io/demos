import render_antd as antd
import render_html as html


def onChange(value):
    print(f"radio checked:{value}")


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
                onChange=onChange,
                defaultValue="a",
            ),
            antd.Radio.Group(
                [
                    antd.Radio.Button("Hangzhou", value="a"),
                    antd.Radio.Button("Shanghai", value="b", disabled=True),
                    antd.Radio.Button("Beijing", value="c"),
                    antd.Radio.Button("Chengdu", value="d"),
                ],
                onChange=onChange,
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
                disabled=True,
                onChange=onChange,
                defaultValue="a",
                style={"marginTop": 16},
            ),
        ]
    )
