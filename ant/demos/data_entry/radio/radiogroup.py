import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    result = antd.Radio.Group(
        [
            antd.Radio("A", value=1),
            antd.Radio("B", value=2),
            antd.Radio("C", value=3),
            antd.Radio("D", value=4),
        ],
        defaultValue=1,
    )
    r.autorun(lambda: print("radio checked", result()))
    return result
