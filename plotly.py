from reflect_plotly import Graph
import plotly.express as px

import plotly.graph_objects as go

fig = go.Figure()

def app():
    fig = px.scatter(
        px.data.iris(),
        x="sepal_width",
        y="sepal_length",
        color="species",
        size="petal_length",
        hover_data=["petal_width"],
    )
    return Graph(fig)
