import render_antd as antd
import render_html as html


def app():
    return antd.Space(
        [
            antd.Typography.Link("Link"),
            antd.Typography.Link("Link"),
            antd.Typography.Link("Link"),
        ],
        split=antd.Divider(type="vertical"),
    )
