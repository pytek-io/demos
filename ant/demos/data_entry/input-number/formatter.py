import render as r
import render_antd as antd
import render_html as html

amount_formatter = r.js_arrow(
    "amount_formatter",
    """(value) => `$ ${value}`.replace(/\\B(?=(\\d{3})+(?!\\d))/g, ",")""",
)
percent_formatter = r.js_arrow("percent_formatter", "(value) => `${value}%`")


def app(_):
    amount_input = antd.InputNumber(defaultValue=1000, formatter=amount_formatter)
    percent_input = antd.InputNumber(
        defaultValue=100, min=0, max=100, formatter=percent_formatter
    )
    r.autorun(lambda: print("amount", amount_input()))
    r.autorun(lambda: print("percent", percent_input()))
    return html.div([amount_input, percent_input])
