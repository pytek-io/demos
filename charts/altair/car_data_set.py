import altair as alt
import render as r
import render_altair as altair
import render_antd as antd
import render_html as html
import vega_datasets

DEFAULT_VALUES = ["Horsepower", "Miles_per_Gallon", "Origin"]
TITLE = "Altair chart"


class App:
    def __init__(self):
        source = vega_datasets.data.cars()
        options = [{"label": name, "value": name} for name in source.columns]
        x, y, color = (
            antd.Select(
                options=options,
                defaultValue=default_value,
                style={"width": 160, "textAlign": "right"},
            )
            for default_value in DEFAULT_VALUES
        )
        r.autoprint(x)
        r.autoprint(y)
        r.autoprint(color)
        self.settings = html.div(
            [
                antd.Row(
                    [
                        antd.Col(
                            html.label(name),
                            style={"width": 60},
                            className="ant-form-item-label",
                        ),
                        antd.Col(element),
                    ],
                    gutter=10,
                    style={"margin": 10},
                )
                for name, element in [("x", x), ("y", y), ("color", color)]
            ],
            style={"marginLeft": 15, "flex": "0 1 auto"},
        )
        brush = alt.selection_interval()

        def spec():
            return (
                alt.Chart(source)
                .mark_circle(size=60)
                .encode(
                    x=x(),
                    y=y(),
                    color=alt.condition(brush, "Origin:N", alt.value("lightgray")),
                    tooltip=["Name", color(), x(), y()],
                )
                .add_selection(brush)
                .properties(width="container", height="container")
            )

        self.content = altair.Chart(
            spec=spec, style={"height": "100%", "width": "100%"}
        )
        self.title = "Car data set"
