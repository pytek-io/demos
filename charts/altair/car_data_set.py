from reflect_altair import Chart
from reflect_antd import Col, Row, Select
from reflect_html import div, label
from vega_datasets import data

import altair as alt

Option = Select.Option

DEFAULT_VALUES = ["Horsepower", "Miles_per_Gallon", "Origin"]
TITLE = "Altair chart"


class App:
    def __init__(self):
        source = data.cars()
        options = [Option(name, value=name) for name in source.columns]
        x, y, color = [
            Select(
                options,
                defaultValue=default_value,
                style=dict(width=160, textAlign="right"),
            )
            for default_value in DEFAULT_VALUES
        ]
        self.settings = div(
            [
                Row(
                    [
                        Col(
                            label(name),
                            style=dict(width=60),
                            className="ant-form-item-label",
                        ),
                        Col(element),
                    ],
                    gutter=10,
                    style=dict(margin=10),
                )
                for name, element in [("x", x), ("y", y), ("color", color)]
            ],
            style={"marginLeft": 15, "flex": "0 1 auto"},
        )

        self.content = Chart(
            spec=lambda: alt.Chart(source)
            .mark_circle(size=60)
            .encode(x=x(), y=y(), color=color(), tooltip=["Name", color(), x(), y()])
            .interactive()
            .properties(width="container", height="container"),
            style={
                "height": "100%",
                "width": "100%",
            },
        )
        self.title = "Car data set"
