import render_antd as antd
import render_html as html

marks = {
    (0): "0°C",
    (26): "26°C",
    (37): "37°C",
    (100): {"style": {"color": "#f50"}, "label": html.strong("100°C")},
}


def app():
    return html.div(
        [
            html.h4("included=true"),
            antd.Slider(marks=marks, defaultValue=37),
            antd.Slider(range=True, marks=marks, defaultValue=[26, 37]),
            html.h4("included=false"),
            antd.Slider(marks=marks, included=False, defaultValue=37),
            html.h4("marks & step"),
            antd.Slider(marks=marks, step=10, defaultValue=37),
            html.h4("step=null"),
            antd.Slider(marks=marks, step=None, defaultValue=37),
        ]
    )
