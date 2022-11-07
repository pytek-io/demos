import reflect_antd as antd
import reflect_html as html

RangePicker = antd.TimePicker.RangePicker


def app():
    return html.div([antd.TimePicker(bordered=False), RangePicker(bordered=False)])
