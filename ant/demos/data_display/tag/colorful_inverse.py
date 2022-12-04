import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Divider("Presets Inverse", orientation="left"),
            html.div(
                [
                    antd.Tag("magenta", color="magenta-inverse"),
                    antd.Tag("red", color="red-inverse"),
                    antd.Tag("volcano", color="volcano-inverse"),
                    antd.Tag("orange", color="orange-inverse"),
                    antd.Tag("gold", color="gold-inverse"),
                    antd.Tag("lime", color="lime-inverse"),
                    antd.Tag("green", color="green-inverse"),
                    antd.Tag("cyan", color="cyan-inverse"),
                    antd.Tag("blue", color="blue-inverse"),
                    antd.Tag("geekblue", color="geekblue-inverse"),
                    antd.Tag("purple", color="purple-inverse"),
                ]
            ),
        ]
    )
