import render as r
import render_antd as antd
import render_html as html

TextArea = antd.Input.TextArea


def app():
    input_ = antd.Input(placeholder="input with clear icon", allowClear=True)
    text_area = TextArea(placeholder="textarea with clear icon", allowClear=True)
    r.autorun(lambda: print(input_()))
    r.autorun(lambda: print(text_area()))
    return html.div([input_, html.br(), html.br(), text_area])
