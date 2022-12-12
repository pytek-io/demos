import reflect_antd as antd
import reflect_html as html


def app():
    check_box = antd.Checkbox("Toggle disabled")
    switch = antd.Switch(disabled=check_box, defaultChecked=True)
    return html.div([switch, html.br(), check_box])
