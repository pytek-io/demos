import reflect as r
import reflect_antd as antd
import reflect_html as html

percent_formatter = r.js_arrow("percent_formatter", "return `${value}%`", "value")


def app():
    return html.div(
        [antd.Slider(formatter=percent_formatter, defaultValue=0), antd.Slider()]
    )
