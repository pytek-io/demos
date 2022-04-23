Fetch historic stock data from [Yahoo Finance](https://finance.yahoo.com/) on the fly. Display data as candle or ohlc charts as well as user defined moving averages. Thanks to the fact that it comply with the pluggable app interface this app can easily be integrated to the [generic dashboard app demo](internal:website.reflect.gallery/demos.dashboard.dashboard).

### Key features
- Fetch data asynchronously from Yahoo Finance.
- Use [Plotly](https://plotly.com/) library
- Update tab name according to inputs
- Control updates to the graph
- Cache heavy computations using `memoize` decorator. 