import reflect as r
import reflect_antd as antd
import reflect_html as html

percent_formatter = r.js_arrow(
    "percent_formatter", "value => `${(value * 100.0).toFixed(2)}%`"
)


def app():
    return html.div(
        [antd.Slider(formatter=percent_formatter, defaultValue=0), antd.Slider()]
    )
