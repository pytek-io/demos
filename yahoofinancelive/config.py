import reflect as r
import reflect_utils


def identity(x):
    return x


def decode_quote(code):
    return QUOTE_TYPES.get(code, "UNKNOWN")


def decode_market_hours(code):
    return MARKET_HOURS_TYPES[code]


QUOTE_TYPES = {
    (0): "NONE",
    (5): "ALTSYMBOL",
    (7): "HEARTBEAT",
    (8): "EQUITY",
    (9): "INDEX",
    (11): "MUTUALFUND",
    (12): "MONEYMARKET",
    (13): "OPTION",
    (14): "CURRENCY",
    (15): "WARRANT",
    (17): "BOND",
    (18): "FUTURE",
    (20): "ETF",
    (23): "COMMODITY",
    (28): "ECNQUOTE",
    (41): "CRYPTOCURRENCY",
    (42): "INDICATOR",
    (1000): "INDUSTRY",
}
MARKET_HOURS_TYPES = [
    "PRE_MARKET",
    "REGULAR_MARKET",
    "POST_MARKET",
    "EXTENDED_HOURS_MARKET",
]
URI = "wss://streamer.finance.yahoo.com/"
DUMMY = "CgRNU0ZUFYVrMUMY0KLMjcNcKgNOTVMwCDgBRZ+B3L9IuPn8CVU0IjRDXYVrMUNlQApHwNgBBA=="
MAX_5_DIGITS = reflect_utils.maximumSignificantDigits(5)
COLUMNS = [
    (
        "id",
        (
            identity,
            {
                "headerName": "Symbol",
                "width": 90,
                "sortable": True,
                "editable": True,
                "enableCellChangeFlash": True,
                "onCellValueChanged": r.Callback(
                    print, args=["data.id", "oldValue", "newValue"]
                ),
                "singleClickEdit": True,
            },
        ),
    ),
    (
        "price",
        (
            identity,
            {
                "headerName": "Price",
                "width": 90,
                "sortable": True,
                "valueNumberFormatter": MAX_5_DIGITS,
                "type": "rightAligned",
            },
        ),
    ),
    (
        "change",
        (
            identity,
            {
                "headerName": "Change",
                "width": 100,
                "sortable": True,
                "valueNumberFormatter": MAX_5_DIGITS,
                "type": "rightAligned",
                "cellStyle": reflect_utils.colorCellNumber,
            },
        ),
    ),
    (
        "changePercent",
        (
            identity,
            {
                "headerName": "Change %",
                "width": 110,
                "sortable": True,
                "valueNumberFormatter": reflect_utils.round_value_to_2_digits,
                "type": "rightAligned",
                "cellStyle": reflect_utils.colorCellNumber,
            },
        ),
    ),
    (
        "time",
        (
            identity,
            {
                "headerName": "Time",
                "width": 90,
                "sortable": True,
                "valueValueFormatter": reflect_utils.compose(
                    reflect_utils.timeStampToJSDate, reflect_utils.toLocaleTimeString
                ),
                "enableCellChangeFlash": True,
            },
        ),
    ),
    (
        "exchange",
        (identity, {"headerName": "Exchange", "width": 100, "sortable": True}),
    ),
    (
        "quoteType",
        (decode_quote, {"headerName": "Type", "width": 90, "sortable": True}),
    ),
    (
        "marketHours",
        (
            decode_market_hours,
            {"headerName": "Market Hours", "width": 120, "sortable": True},
        ),
    ),
    (
        "dayVolume",
        (
            identity,
            {
                "headerName": "Day Volume",
                "width": 120,
                "sortable": True,
                "valueNumberFormatter": reflect_utils.toLocaleString,
                "type": "rightAligned",
            },
        ),
    ),
]
