import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    radio_group = antd.Radio.Group(
        [antd.Radio("Option A", value="a"), antd.Radio("Option B", value="b")],
        defaultValue="a",
    )
    r.autorun(lambda: print("selected", radio_group()))
    return radio_group
