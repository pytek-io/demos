import render as r
import render_antd as antd
import render_html as html


def app(_):
    radio_group = antd.Radio.Group(
        [antd.Radio("Option A", value="a"), antd.Radio("Option B", value="b")],
        defaultValue="a",
    )
    r.autorun(lambda: print("selected", radio_group()))
    return radio_group
