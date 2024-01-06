import render_antd as antd
import render_html as html


def app():
    contentStyle = {
        "height": "160px",
        "color": "#fff",
        "lineHeight": "160px",
        "textAlign": "center",
        "background": "#364d79",
    }
    return antd.Carousel(
        [
            html.div(html.h3("1", style=contentStyle)),
            html.div(html.h3("2", style=contentStyle)),
            html.div(html.h3("3", style=contentStyle)),
            html.div(html.h3("4", style=contentStyle)),
        ],
        effect="fade",
    )
