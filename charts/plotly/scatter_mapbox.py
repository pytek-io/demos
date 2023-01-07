import pathlib

import plotly.express as px
import reflect_plotly as plotly


def app():
    print(pathlib.Path(__file__).parent)
    px.set_mapbox_access_token(
        pathlib.Path(pathlib.Path(__file__).parent, ".mapbox_token").read_text()
    )
    return plotly.Graph(
        px.scatter_mapbox(
            px.data.carshare(),
            lat="centroid_lat",
            lon="centroid_lon",
            color="peak_hour",
            size="car_hours",
            color_continuous_scale=px.colors.cyclical.IceFire,
            size_max=15,
            zoom=10,
        )
    )
