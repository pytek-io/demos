from reflect_html import *
from reflect_antd import Avatar


def app():
    return div(
        [
            Avatar("A", shape="circle", src="http://abc.com/not-exist.jpg"),
            Avatar("ABC", shape="circle", src="http://abc.com/not-exist.jpg"),
        ]
    )
