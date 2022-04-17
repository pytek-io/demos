from reflect_plotly import Graph
import plotly.express as px


def app():
    return Graph(
        px.scatter(
            px.data.iris(),
            x="sepal_width",
            y="sepal_length",
            color="species",
            size="petal_length",
            hover_data=["petal_width"],
        )
    )
