from reflect_html import *
from reflect_antd import Select

from reflect import autorun

Option = Select.Option


def app():
    select = Select(
        [
            Option(
                div(
                    [span("🇨🇳", role="img", ariaLabel="China"), "China (中国)"],
                    className="demo-option-label-item",
                ),
                value="china",
                label="China",
            ),
            Option(
                div(
                    [span("🇺🇸", role="img", ariaLabel="USA"), "USA (美国)"],
                    className="demo-option-label-item",
                ),
                value="usa",
                label="USA",
            ),
            Option(
                div(
                    [span("🇯🇵", role="img", ariaLabel="Japan"), "Japan (日本)"],
                    className="demo-option-label-item",
                ),
                value="japan",
                label="Japan",
            ),
            Option(
                div(
                    [span("🇰🇷", role="img", ariaLabel="Korea"), "Korea (韩国)"],
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
    autorun(lambda: print(select()))
    return select
