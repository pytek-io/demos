import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    size = antd.Radio.Group(
        [
            antd.Radio.Button("Large", value="large", key="large"),
            antd.Radio.Button("Default", value="default", key="default"),
            antd.Radio.Button("Small", value="small", key="small"),
        ],
        defaultValue="default",
    )
    r.autoprint(size)
    return html.div([size, antd.Button("Primary", type="primary", size=size)])