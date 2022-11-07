import reflect as r
import reflect_antd as antd
import reflect_html as html

Option = antd.Select.Option


def app():
    select = antd.Select(
        [
            Option(
                html.div(
                    [html.span("🇨🇳", role="img", ariaLabel="China"), "China (中国)"],
                    className="demo-option-label-item",
                ),
                value="china",
                label="China",
            ),
            Option(
                html.div(
                    [html.span("🇺🇸", role="img", ariaLabel="USA"), "USA (美国)"],
                    className="demo-option-label-item",
                ),
                value="usa",
                label="USA",
            ),
            Option(
                html.div(
                    [html.span("🇯🇵", role="img", ariaLabel="Japan"), "Japan (日本)"],
                    className="demo-option-label-item",
                ),
                value="japan",
                label="Japan",
            ),
            Option(
                html.div(
                    [html.span("🇰🇷", role="img", ariaLabel="Korea"), "Korea (韩国)"],
                    className="demo-option-label-item",
                ),
                value="korea",
                label="Korea",
            ),
        ],
        mode="multiple",
        style=dict(width="100%"),
        placeholder="select one country",
        defaultValue=["china"],
        optionLabelProp="label",
    )
    r.autorun(lambda: print(select()))
    return select
