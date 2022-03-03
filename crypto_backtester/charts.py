import pickle
from datetime import datetime

from reflect_altair import Chart
from reflect_html import div
import altair as alt
import pandas as pd

GREEN = "#06982d"
BLUE = "#5276A7"
RED = "#ae1325"
DARK_BLUE = "#2E2252"
ORANGE = "#FF6600"


def create_candle_sticks(df, open_name, close_name, low_name, high_name):
    open_close_color = alt.condition(
        f"datum.{open_name} <= datum.{close_name}",
        alt.value(GREEN),
        alt.value(RED),
    )
    ohlc_base = alt.Chart(df).encode(alt.X("ticks:T"), color=open_close_color)
    low_high = ohlc_base.mark_rule().encode(
        alt.Y(f"{low_name}:Q", title=None), alt.Y2(f"{high_name}:Q")
    )
    open_close = ohlc_base.mark_bar().encode(
        alt.Y(f"{open_name}:Q"), alt.Y2(f"{close_name}:Q")
    )
    return low_high + open_close


def create_spot_and_pl_graph(df):
    base = (
        alt.Chart(df)
        .transform_fold(
            ["close_spot", "open_option", "close_option", "ivol_mid", "volume_option"],
            as_=["Measure", "Value"],
        )
        .encode(
            alt.Color("Measure:N", legend=None),
            alt.X("ticks:T", axis=alt.Axis(format="%d/%m", labelAngle=-45, title=None)),
        )
    )


def create_y_axis(title, titleColor):
    return alt.Y(
        "Value:Q",
        axis=alt.Axis(title=title, titleColor=titleColor),
        scale=alt.Scale(zero=False),
    )


def create_performance_chart(df: pd.DataFrame, strike):
    base = (
        alt.Chart(df)
        .transform_fold(
            ["close_spot", "open_option", "close_option", "ivol_mid", "volume_option"],
            as_=["Measure", "Value"],
        )
        .encode(
            alt.Color("Measure:N", legend=None),
            alt.X("ticks:T", axis=alt.Axis(format="%d/%m", labelAngle=-45, title=None)),
        )
    )
    close_spot = (
        base.mark_line(interpolate="step-after")
        .transform_filter(alt.datum.Measure == "close_spot")
        .encode(create_y_axis("spot", BLUE), color=alt.value(BLUE))
    )
    close_option = (
        base.mark_line(interpolate="step-after")
        .transform_filter(alt.datum.Measure == "close_option")
        .encode(create_y_axis("option", GREEN), color=alt.value(GREEN))
    )
    if strike:
        close_spot += (
            alt.Chart(pd.DataFrame({"y": [strike]}))
            .mark_rule(strokeDash=[10, 10])
            .encode(y="y")
        )
    volume = (
        base.mark_bar()
        .transform_filter(alt.datum.Measure == "volume_option")
        .encode(create_y_axis("volume", DARK_BLUE), color=alt.value(DARK_BLUE))
    )
    ivol_mid = (
        base.mark_line(interpolate="step-after")
        .transform_filter(alt.datum.Measure == "ivol_mid")
        .encode(create_y_axis("implied vol", ORANGE), color=alt.value(ORANGE))
    )
    return alt.vconcat(
        *[
            alt.layer(*encodings)
            .resolve_scale(y="independent")
            .interactive()
            .properties(height="container", width="container")
            for encodings in [
                [close_spot, close_option],
                [ivol_mid, volume],
            ]
        ],
    )


def app(instrument_name="BTC-24JUN22-30000-C"):
    """ "Display data for instrument saved in main"""
    df = pickle.loads(open(f"{instrument_name}.pick", "rb").read())
    _, expiry, strike, option_type = instrument_name.split("-")
    expiry, option_type = datetime.strptime(expiry, "%d%b%y"), option_type.lower()
    return div(
        Chart(
            create_performance_chart(df, int(strike)),
            style={
                # magic numbers to get altair.vconcat to dimension charts correctly (responsiveness is broken as charts size incread by a factor of two...)
                "height": "40%",
                "width": "90%",
            },
        ),
        style={
            "position": "absolute",
            "height": "95%",
            "width": "95%",
            "paddingTop": 20,
        },
    )
