from reflect_plotly import Graph
import plotly.express as px


def app():
    px.set_mapbox_access_token(open(".mapbox_token").read())
    return Graph(
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
