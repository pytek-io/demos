def scatter(timeseries, color):
    return go.Scatter(
        name=timeseries.name,
        line={"color": color},
        x=timeseries.values["date"],
        y=timeseries.values["value"],
    )


def moving_average(stock: TimeSeries, nb_days: int, color: str):
    return go.Scatter(
        name=f"MVA {stock.ticker} {nb_days} days",
        line={"color": color},
        x=stock.values["Date"],
        y=stock.values["Close"].rolling(nb_days).mean(),
    )


def candle_stick(yahoo_timeseries: TimeSeries):
    return go.Candlestick(
        x=yahoo_timeseries.values["Date"],
        decreasing={"line": {"color": "cyan"}},
        increasing={"line": {"color": "gray"}},
        xaxis="x",
        yaxis="y",
        name=yahoo_timeseries.ticker,
        open=yahoo_timeseries.values["Open"],
        close=yahoo_timeseries.values["Close"],
        low=yahoo_timeseries.values["Low"],
        high=yahoo_timeseries.values["High"],
    )


# Create figure with secondary y-axis
figure = make_subplots(specs=[[{"secondary_y": True}]])
mv_1 = moving_average(stock_1, 2, "blue")
mv_2 = moving_average(stock_1, 10, "yellow")

figure.add_trace(candle_stick(stock_1), secondary_y=False)


figure.add_annotation(
    x=datetime.date(2022, 7, 1), y=150, text="sth happened here!", showarrow=True, arrowhead=1
)

figure.add_trace(scatter(stock_2, "red"), secondary_y=True)
figure.update_layout(title_text="Double Y Axis Example", title_x=0.5)
# figure.update_xaxes(title_text="xaxis title")
figure.update_yaxes(title_text="<b>Stock price</b> USD", secondary_y=False)
figure.update_yaxes(title_text="<b>Rate</b> percent", secondary_y=True)
