def moving_average(stock, nb_days: int, color: str):
    return go.Scatter(
        name=f"MVA {stock.ticker} {nb_days} days",
        line={"color": color},
        x=stock.values["Date"],
        y=stock.values["Close"].rolling(nb_days).mean(),
    )


def candle_stick(df):
    return go.Candlestick(
        x=df.values["Date"],
        decreasing={"line": {"color": "cyan"}},
        increasing={"line": {"color": "gray"}},
        xaxis="x",
        yaxis="y",
        name=df.ticker,
        open=df.values["Open"],
        close=df.values["Close"],
        low=df.values["Low"],
        high=df.values["High"],
    )


stock1_plot = candle_stick(stock_1)
mv_1 = moving_average(stock_1, 2, "blue")
mv_2 = moving_average(stock_1, 10, "yellow")

figure = go.Figure([stock1_plot])
figure.add_annotation(
    x=datetime.date(2022, 7, 1), y=150, text="hello", showarrow=True, arrowhead=1
)
