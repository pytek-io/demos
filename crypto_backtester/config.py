import pandas
from reflect import JSMethod
from reflect_aggrid import ColumnDetails

timeStampTimeFormatter = JSMethod(
    "amount_formatter",
    "return new Date(value.value).toLocaleDateString()",
    "value",
)


def to_timestamp(d):
    return int(pandas.to_datetime(d).timestamp()) * 1000


INSTRUMENT_HISTORY = [
    ColumnDetails(
        header_name="Open",
        field="open",
        type="rightAligned",
    ),
    ColumnDetails(
        header_name="Close",
        field="close",
        type="rightAligned",
    ),
    ColumnDetails(
        header_name="Ticks",
        field="ticks",
        type="rightAligned",
        formatter=timeStampTimeFormatter,
    ),
    ColumnDetails(
        header_name="Volume",
        field="volume",
        type="rightAligned",
    ),
    ColumnDetails(
        header_name="Low",
        field="low",
        type="rightAligned",
    ),
    ColumnDetails(
        header_name="High",
        field="high",
        type="rightAligned",
    ),
]

INSTRUMENTS = [
    ColumnDetails(
        header_name="Instrument Name",
        field="instrument_name",
        width=180,
    ),
    ColumnDetails(
        header_name="Option",
        field="option_type",
        width=80,
    ),
    ColumnDetails(header_name="Strike", field="strike", width=80),
    ColumnDetails(
        header_name="Expiration",
        field="expiration_timestamp",
        formatter=timeStampTimeFormatter,
        sorting_order=["desc"],
    ),
    ColumnDetails(header_name="Tick", field="tick_size", width=70),
    ColumnDetails(
        header_name="Settlement Period",
        field="settlement_period",
        width=90,
    ),
    ColumnDetails(
        header_name="Currency",
        field="quote_currency",
        width=80,
    ),
    ColumnDetails(
        header_name="Min Trade Amount",
        field="min_trade_amount",
        width=80,
    ),
    ColumnDetails(header_name="Kind", field="kind", width=70),
    ColumnDetails(
        header_name="Active",
        field="is_active",
        preprocess=lambda x: x == "true",
        width=70,
    ),
    ColumnDetails(
        header_name="Creation",
        field="creation_timestamp",
        formatter=timeStampTimeFormatter,
    ),
    # Column(
    #     header_name="Commission",
    #     children=(
    #         Column(
    #             header_name="Taker Commission",
    #             field="taker_commission",
    #             width=70,
    #             preprocess=bps,
    #         ),
    #         Column(
    #             header_name="Maker Commission",
    #             field="maker_commission",
    #             width=70,
    #             preprocess=bps,
    #         ),
    #         Column(
    #             header_name="Block Trade Commission",
    #             field="block_trade_commission",
    #             width=70,
    #             preprocess=bps,
    #         ),
    #     ),
    # ),
    ColumnDetails(
        header_name="Currency",
        field="base_currency",
    ),
    ColumnDetails(
        header_name="Contract Size",
        field="contract_size",
    ),
    # Column(
    #     header_name="Creation Time",
    #     field="creation_time",
    #     width=170,
    # ),
    # Column(
    #     header_name="Expiration Time",
    #     field="expiration_time",
    #     width=170,
    # ),
]
