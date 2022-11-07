import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Space(
        [
            antd.Typography.Link("Link"),
            antd.Typography.Link("Link"),
            antd.Typography.Link("Link"),
        ],
        split=antd.Divider(type="vertical"),
    )
