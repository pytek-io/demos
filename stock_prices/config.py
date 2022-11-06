from reflect_utils import round_value_to_2_digits_col, toLocaleString


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
    (
        "symbol",
        (
            identity,
            dict(
                headerName="Symbol",
                width=90,
                sortable=True,
            ),
        ),
    ),
    (
        "lastsale",
        (
            parse_dollar_amount,
            dict(
                headerName="Last Sale",
                width=100,
                sortable=True,
            ),
        ),
    ),
    (
        "netchange",
        (
            identity,
            dict(
                headerName="Change",
                width=100,
                sortable=True,
            ),
        ),
    ),
    (
        "pctchange",
        (
            parse_percentage,
            dict(
                headerName="% Change",
                width=110,
                sortable=True,
                valueFormatter=round_value_to_2_digits_col,
            ),
        ),
    ),
    (
        "marketCap",
        (
            convert_to_integer,
            dict(
                headerName="Mkt Cap",
                width=140,
                sortable=True,
                valueValueFormatter=toLocaleString,
            ),
        ),
    ),
    (
        "name",
        (
            identity,
            dict(
                headerName="Name",
                width=300,
                sortable=True,
            ),
        ),
    ),
)
