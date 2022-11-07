import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Button("Primary", type="primary", ghost=True),
            antd.Button("Default", ghost=True),
            antd.Button("Dashed", type="dashed", ghost=True),
        ],
        className="site-button-ghost-wrapper",
    )
