import altair as alt
import render_altair as altair
import vega_datasets

TITLE = "US airports"


def app(_):
    airports = vega_datasets.data.airports.url
    flights_airport = vega_datasets.data.flights_airport.url
    states = alt.topo_feature(vega_datasets.data.us_10m.url, feature="states")
    select_city = alt.selection_single(
        on="mouseover", nearest=True, fields=["origin"], empty="none"
    )
    lookup_data = alt.LookupData(
        airports, key="iata", fields=["state", "latitude", "longitude"]
    )
    background = (
        alt.Chart(states)
        .mark_geoshape(fill="lightgray", stroke="white")
        .properties(width=750, height=500)
        .project("albersUsa")
    )
    connections = (
        alt.Chart(flights_airport)
        .mark_rule(opacity=0.35)
        .encode(
            latitude="latitude:Q",
            longitude="longitude:Q",
            latitude2="lat2:Q",
            longitude2="lon2:Q",
        )
        .transform_lookup(lookup="origin", from_=lookup_data)
        .transform_lookup(
            lookup="destination", from_=lookup_data, as_=["state", "lat2", "lon2"]
        )
        .transform_filter(select_city)
    )
    points = (
        alt.Chart(flights_airport)
        .mark_circle()
        .encode(
            latitude="latitude:Q",
            longitude="longitude:Q",
            size=alt.Size("routes:Q", scale=alt.Scale(range=[0, 1000]), legend=None),
            order=alt.Order("routes:Q", sort="descending"),
            tooltip=["origin:N", "routes:Q"],
        )
        .transform_aggregate(routes="count()", groupby=["origin"])
        .transform_lookup(lookup="origin", from_=lookup_data)
        .transform_filter((alt.datum.state != "PR") & (alt.datum.state != "VI"))
        .add_selection(select_city)
    )
    return altair.Chart(
        spec=background + connections + points,
        style={"height": "100%", "width": "100%"},
    )
