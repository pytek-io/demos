from reflect_html import *
from reflect_antd import Select

from reflect import autorun

Option = Select.Option


def app():
    select = Select(
        [
            Option(
                div(
                    [span("π¨π³", role="img", ariaLabel="China"), "China (δΈ­ε½)"],
                    className="demo-option-label-item",
                ),
                value="china",
                label="China",
            ),
            Option(
                div(
                    [span("πΊπΈ", role="img", ariaLabel="USA"), "USA (ηΎε½)"],
                    className="demo-option-label-item",
                ),
                value="usa",
                label="USA",
            ),
            Option(
                div(
                    [span("π―π΅", role="img", ariaLabel="Japan"), "Japan (ζ₯ζ¬)"],
                    className="demo-option-label-item",
                ),
                value="japan",
                label="Japan",
            ),
            Option(
                div(
                    [span("π°π·", role="img", ariaLabel="Korea"), "Korea (ι©ε½)"],
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
