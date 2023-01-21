import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    select = antd.Select(
        options=[
            {
                "label": html.div(
                    [html.span("🇨🇳", role="img", ariaLabel="China"), "China (中国)"],
                    className="demo-option-label-item",
                ),
                "value": "china",
                "label": "China",
            },
            {
                "label": html.div(
                    [html.span("🇺🇸", role="img", ariaLabel="USA"), "USA (美国)"],
                    className="demo-option-label-item",
                ),
                "value": "usa",
                "label": "USA",
            },
            {
                "label": html.div(
                    [html.span("🇯🇵", role="img", ariaLabel="Japan"), "Japan (日本)"],
                    className="demo-option-label-item",
                ),
                "value": "japan",
                "label": "Japan",
            },
            {
                "label": html.div(
                    [html.span("🇰🇷", role="img", ariaLabel="Korea"), "Korea (韩国)"],
                    className="demo-option-label-item",
                ),
                "value": "korea",
                "label": "Korea",
            },
        ],
        mode="multiple",
        style={"width": "100%"},
        placeholder="select one country",
        defaultValue=["china"],
        optionLabelProp="label",
    )
    r.autorun(lambda: print(select()))
    return select
