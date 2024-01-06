import render as r
import render_antd as antd
import render_html as html

plain_options = ["Apple", "Pear", "Orange"]
options = [
    {"label": "Apple", "value": "Apple"},
    {"label": "Pear", "value": "Pear"},
    {"label": "Orange", "value": "Orange"},
]
options_with_disabled = [
    {"label": "Apple", "value": "Apple"},
    {"label": "Pear", "value": "Pear"},
    {"label": "Orange", "value": "Orange", "disabled": True},
]


def app():
    radio_group1 = antd.Radio.Group(options=plain_options, defaultValue="Apple")
    radio_group2 = antd.Radio.Group(options=options_with_disabled, defaultValue="Apple")
    radio_group3 = antd.Radio.Group(
        options=options, defaultValue="Apple", optionType="button"
    )
    radio_group4 = antd.Radio.Group(
        options=options_with_disabled,
        defaultValue="Apple",
        optionType="button",
        buttonStyle="solid",
    )
    r.autorun(lambda: print("radio1 checked", radio_group1()))
    r.autorun(lambda: print("radio2 checked", radio_group2()))
    r.autorun(lambda: print("radio3 checked", radio_group3()))
    r.autorun(lambda: print("radio4 checked", radio_group4()))
    return html.div(
        [
            radio_group1,
            html.br(),
            radio_group2,
            html.br(),
            html.br(),
            radio_group3,
            html.br(),
            html.br(),
            radio_group4,
        ]
    )
