import altair as alt
import reflect_altair as altair
import reflect_antd as antd
import reflect_html as html
import vega_datasets

Option = antd.Select.Option
DEFAULT_VALUES = ["Horsepower", "Miles_per_Gallon", "Origin"]
TITLE = "Altair chart"


class App:
    def __init__(self):
        source = vega_datasets.data.cars()
        options = [Option(name, value=name) for name in source.columns]
        x, y, color = [
            antd.Select(
                options,
                defaultValue=default_value,
                style=dict(width=160, textAlign="right"),
            )
            for default_value in DEFAULT_VALUES
        ]
        self.settings = html.div(
            [
                antd.Row(
                    [
                        antd.Col(
                            html.label(name),
                            style=dict(width=60),
                            className="ant-form-item-label",
                        ),
                        antd.Col(element),
                    ],
                    gutter=10,
                    style=dict(margin=10),
                )
                for name, element in [("x", x), ("y", y), ("color", color)]
            ],
            style={"marginLeft": 15, "flex": "0 1 auto"},
        )
        brush = alt.selection_interval()
        self.content = altair.Chart(
            spec=lambda: alt.Chart(source)
            .mark_circle(size=60)
            .encode(
                x=x(),
                y=y(),
                color=alt.condition(brush, "Origin:N", alt.value("lightgray")),
                tooltip=["Name", color(), x(), y()],
            )
            .add_selection(brush)
            .properties(width="container", height="container"),
            style={"height": "100%", "width": "100%"},
        )
        self.title = "Car data set"
