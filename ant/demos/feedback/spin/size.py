import render_antd as antd
import render_html as html


def app():
    return antd.Space(
        [antd.Spin(size="small"), antd.Spin(), antd.Spin(size="large")], size="middle"
    )
