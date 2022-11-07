import pandas
import reflect as r
import reflect_aggrid as aggrid

timeStampTimeFormatter = r.JSMethod(
    "amount_formatter", "return new Date(value.value).toLocaleDateString()", "value"
)


def to_timestamp(d):
    return int(pandas.to_datetime(d).timestamp()) * 1000


INSTRUMENT_HISTORY = [
    aggrid.ColumnDetails(header_name="Open", field="open", type="rightAligned"),
    aggrid.ColumnDetails(header_name="Close", field="close", type="rightAligned"),
    aggrid.ColumnDetails(
        header_name="Ticks",
        field="ticks",
        type="rightAligned",
        formatter=timeStampTimeFormatter,
    ),
    aggrid.ColumnDetails(header_name="Volume", field="volume", type="rightAligned"),
    aggrid.ColumnDetails(header_name="Low", field="low", type="rightAligned"),
    aggrid.ColumnDetails(header_name="High", field="high", type="rightAligned"),
]
INSTRUMENTS = [
    aggrid.ColumnDetails(
        header_name="Instrument Name", field="instrument_name", width=180
    ),
    aggrid.ColumnDetails(header_name="Option", field="option_type", width=80),
    aggrid.ColumnDetails(header_name="Strike", field="strike", width=80),
    aggrid.ColumnDetails(
        header_name="Expiration",
        field="expiration_timestamp",
        formatter=timeStampTimeFormatter,
        sorting_order=["desc"],
    ),
    aggrid.ColumnDetails(header_name="Tick", field="tick_size", width=70),
    aggrid.ColumnDetails(
        header_name="Settlement Period", field="settlement_period", width=90
    ),
    aggrid.ColumnDetails(header_name="Currency", field="quote_currency", width=80),
    aggrid.ColumnDetails(
        header_name="Min Trade Amount", field="min_trade_amount", width=80
    ),
    aggrid.ColumnDetails(header_name="Kind", field="kind", width=70),
    aggrid.ColumnDetails(
        header_name="Active",
        field="is_active",
        preprocess=lambda x: x == "true",
        width=70,
    ),
    aggrid.ColumnDetails(
        header_name="Creation",
        field="creation_timestamp",
        formatter=timeStampTimeFormatter,
    ),
    aggrid.ColumnDetails(header_name="Currency", field="base_currency"),
    aggrid.ColumnDetails(header_name="Contract Size", field="contract_size"),
]
