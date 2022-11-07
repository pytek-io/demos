import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Space(
        [antd.Button("Button", key=index) for index in range(20)],
        size=[8, 16],
        wrap=True,
    )
