import plotly.express as px
import reflect_plotly as plotly


def app():
    return plotly.Graph(
        px.scatter(
            px.data.iris(),
            x="sepal_width",
            y="sepal_length",
            color="species",
            size="petal_length",
            hover_data=["petal_width"],
        )
    )
