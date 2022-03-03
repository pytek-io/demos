from reflect_html import div
from reflect_antd import InputNumber
from reflect import JSMethod, autorun

amount_formatter = JSMethod(
    "amount_formatter",
    'return `$ ${value}`.replace(/\B(?=(\d{3})+(?!\d))/g, ",")',
    "value",
)

percent_formatter = JSMethod(
    "percent_formatter",
    "return `${value}%`",
    "value",
)


def app():
    amount_input = InputNumber(
        defaultValue=1000, formatter=amount_formatter
    )
    percent_input = InputNumber(
        defaultValue=100,
        min=0,
        max=100,
        formatter=percent_formatter,
    )
    autorun(lambda: print("amount", amount_input()))
    autorun(lambda: print("percent", percent_input()))
    return div([amount_input, percent_input])
