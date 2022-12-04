import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Divider("Presets", orientation="left"),
            html.div(
                [
                    antd.Tag("magenta", color="magenta"),
                    antd.Tag("red", color="red"),
                    antd.Tag("volcano", color="volcano"),
                    antd.Tag("orange", color="orange"),
                    antd.Tag("gold", color="gold"),
                    antd.Tag("lime", color="lime"),
                    antd.Tag("green", color="green"),
                    antd.Tag("cyan", color="cyan"),
                    antd.Tag("blue", color="blue"),
                    antd.Tag("geekblue", color="geekblue"),
                    antd.Tag("purple", color="purple"),
                ]
            ),
            antd.Divider("Custom", orientation="left"),
            html.div(
                [
                    antd.Tag("#f50", color="#f50"),
                    antd.Tag("#2db7f5", color="#2db7f5"),
                    antd.Tag("#87d068", color="#87d068"),
                    antd.Tag("#108ee9", color="#108ee9"),
                ]
            ),
        ]
    )
