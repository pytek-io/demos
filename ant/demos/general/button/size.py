import reflect as r
import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    size = antd.Radio.Group(
        [
            antd.Radio.Button("Large", value="large"),
            antd.Radio.Button("Default", value="default"),
            antd.Radio.Button("Small", value="small"),
        ],
        defaultValue="small",
    )
    r.autorun(lambda: print(size()))
    return html.div([size, antd.Button("Primary", type="primary", size=size)])
