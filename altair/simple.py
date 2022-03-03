import altair as alt
from vega_datasets import data
from reflect_altair import Chart


def app():
    return Chart(
        alt.Chart(data.cars())
        .mark_circle(size=60)
        .encode(
            x="Horsepower",
            y="Miles_per_Gallon",
            color="Origin",
            tooltip=["Name", "Origin", "Horsepower", "Miles_per_Gallon"],
        ),
    )
