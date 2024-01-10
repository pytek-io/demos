import render_antd as antd
import render_html as html

RangePicker = antd.TimePicker.RangePicker


def app(_):
    return html.div([antd.TimePicker(bordered=False), RangePicker(bordered=False)])
