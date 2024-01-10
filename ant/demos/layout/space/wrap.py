import render_antd as antd
import render_html as html


def app(_):
    return antd.Space(
        [antd.Button("Button", key=index) for index in range(20)],
        size=[8, 16],
        wrap=True,
    )
