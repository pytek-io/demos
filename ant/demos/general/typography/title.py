import reflect_antd as antd
import reflect_html as html

Title = antd.Typography.Title


def app():
    return html.div(
        [
            Title("h1. Ant Design"),
            Title("h2. Ant Design", level=2),
            Title("h3. Ant Design", level=3),
            Title("h4. Ant Design", level=4),
            Title("h5. Ant Design", level=5),
        ]
    )
