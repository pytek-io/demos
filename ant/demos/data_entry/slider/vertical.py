import render_antd as antd
import render_html as html

style = {"display": "inline-block", "height": 300, "marginLeft": 70}
marks = {
    (0): "0°C",
    (26): "26°C",
    (37): "37°C",
    (100): {"style": {"color": "#f50"}, "label": html.strong("100°C")},
}


def app(_):
    return html.div(
        [
            html.div(antd.Slider(vertical=True, defaultValue=30), style=style),
            html.div(
                antd.Slider(vertical=True, range=True, step=10, defaultValue=[20, 50]),
                style=style,
            ),
            html.div(
                antd.Slider(
                    vertical=True, range=True, marks=marks, defaultValue=[26, 37]
                ),
                style=style,
            ),
        ]
    )
