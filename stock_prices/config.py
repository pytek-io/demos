from reflect_utils import (
    round_value_to_2_digits_col,
    toLocaleString,
    transform_if_number,
)


def identity(value):
    return value


def parse_float(value):
    return float(value.replace(",", "")) if value != "-" else 0.0


def parse_dollar_amount(value):
    return parse_float(value[1:])


def parse_percentage(value):
    return parse_float(value[:-1])


def convert_to_integer(value):
    return int(parse_float(value)) if value != "NA" else 0


COLUMNS = (
    ("symbol", {"headerName": "Symbol", "width": 90, "sortable": True}),
    ("lastsale", {"headerName": "Last Sale", "width": 100, "sortable": True}),
    ("netchange", {"headerName": "Change", "width": 100, "sortable": True}),
    (
        "pctchange",
        {
            "headerName": "% Change",
            "width": 110,
            "sortable": True,
            "valueFormatter": round_value_to_2_digits_col,
        },
    ),
    (
        "marketCap",
        {
            "headerName": "Mkt Cap",
            "width": 140,
            "sortable": True,
            "valueFormatter": transform_if_number(toLocaleString),
        },
    ),
    ("name", {"headerName": "Name", "width": 300, "sortable": True}),
)
