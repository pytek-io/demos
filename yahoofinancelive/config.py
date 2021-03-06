from reflect.utils import identity
from reflect_utils.formatters import (
    colorCellNumber,
    compose,
    maximumSignificantDigits,
    round_value_to_2_digits,
    timeStampToJSDate,
    toLocaleString,
    toLocaleTimeString,
)
from reflect import Callback

def decode_quote(code):
    return QUOTE_TYPES.get(code, "UNKNOWN")


def decode_market_hours(code):
    return MARKET_HOURS_TYPES[code]


QUOTE_TYPES = {
    0: "NONE",
    5: "ALTSYMBOL",
    7: "HEARTBEAT",
    8: "EQUITY",
    9: "INDEX",
    11: "MUTUALFUND",
    12: "MONEYMARKET",
    13: "OPTION",
    14: "CURRENCY",
    15: "WARRANT",
    17: "BOND",
    18: "FUTURE",
    20: "ETF",
    23: "COMMODITY",
    28: "ECNQUOTE",
    41: "CRYPTOCURRENCY",
    42: "INDICATOR",
    1000: "INDUSTRY",
}

MARKET_HOURS_TYPES = [
    "PRE_MARKET",
    "REGULAR_MARKET",
    "POST_MARKET",
    "EXTENDED_HOURS_MARKET",
]

URI = "wss://streamer.finance.yahoo.com/"
DUMMY = "CgRNU0ZUFYVrMUMY0KLMjcNcKgNOTVMwCDgBRZ+B3L9IuPn8CVU0IjRDXYVrMUNlQApHwNgBBA=="
MAX_5_DIGITS = maximumSignificantDigits(5)
COLUMNS = [
    (
        "id",
        (
            identity,
            dict(
                headerName="Symbol",
                width=90,
                sortable=True,
                editable=True,
                enableCellChangeFlash=True,
                onCellValueChanged=Callback(print, args=["data.id", "oldValue", "newValue"]),
                singleClickEdit=True,
            ),
        ),
    ),
    (
        "price",
        (
            identity,
            dict(
                headerName="Price",
                width=90,
                sortable=True,
                valueNumberFormatter=MAX_5_DIGITS,
                type="rightAligned",
            ),
        ),
    ),
    (
        "change",
        (
            identity,
            dict(
                headerName="Change",
                width=100,
                sortable=True,
                valueNumberFormatter=MAX_5_DIGITS,
                type="rightAligned",
                cellStyle=colorCellNumber,
            ),
        ),
    ),
    (
        "changePercent",
        (
            identity,
            dict(
                headerName="Change %",
                width=110,
                sortable=True,
                valueNumberFormatter=round_value_to_2_digits,
                type="rightAligned",
                cellStyle=colorCellNumber,
            ),
        ),
    ),
    (
        "time",
        (
            identity,
            dict(
                headerName="Time",
                width=90,
                sortable=True,
                valueValueFormatter=compose(timeStampToJSDate, toLocaleTimeString),
                enableCellChangeFlash=True,
            ),
        ),
    ),
    (
        "exchange",
        (
            identity,
            dict(
                headerName="Exchange",
                width=100,
                sortable=True,
            ),
        ),
    ),
    (
        "quoteType",
        (
            decode_quote,
            dict(
                headerName="Type",
                width=90,
                sortable=True,
            ),
        ),
    ),
    (
        "marketHours",
        (
            decode_market_hours,
            dict(
                headerName="Market Hours",
                width=120,
                sortable=True,
            ),
        ),
    ),
    (
        "dayVolume",
        (
            identity,
            dict(
                headerName="Day Volume",
                width=120,
                sortable=True,
                valueNumberFormatter=toLocaleString,
                type="rightAligned",
            ),
        ),
    ),
]
