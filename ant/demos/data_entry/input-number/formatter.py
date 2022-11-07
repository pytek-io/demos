import reflect as r
import reflect_antd as antd
import reflect_html as html

amount_formatter = r.JSMethod(
    "amount_formatter",
    'return `$ ${value}`.replace(/\\B(?=(\\d{3})+(?!\\d))/g, ",")',
    "value",
)
percent_formatter = r.JSMethod("percent_formatter", "return `${value}%`", "value")


def app():
    amount_input = antd.InputNumber(defaultValue=1000, formatter=amount_formatter)
    percent_input = antd.InputNumber(
        defaultValue=100, min=0, max=100, formatter=percent_formatter
    )
    r.autorun(lambda: print("amount", amount_input()))
    r.autorun(lambda: print("percent", percent_input()))
    return html.div([amount_input, percent_input])
