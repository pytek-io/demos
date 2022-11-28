import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Avatar("A", shape="circle", src="http://abc.com/not-exist.jpg"),
            antd.Avatar("ABC", shape="circle", src="http://abc.com/not-exist.jpg"),
        ]
    )
