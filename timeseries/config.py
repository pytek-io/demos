from render_utils import round_value_to_2_digits_col, toLocaleString


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


COLUMNS = ("date", (identity, {"headerName": "Date", "width": 90, "sortable": True})), (
    "value",
    (identity, {"headerName": "Value", "width": 100, "sortable": True}),
)
