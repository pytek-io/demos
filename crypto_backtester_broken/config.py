from datetime import datetime
from dataclasses import dataclass
from typing import Callable, List, Optional, Tuple, TypeVar

import pandas
from reflect import js
from .utils import bps


@dataclass
class Column:
    """Class for keeping track of an item in inventory."""

    header_name: str
    field: Optional[str] = None
    formatter: Optional[Callable] = None
    preprocess: Optional[Callable] = None
    width: Optional[Callable] = 100
    type: str = "rightAligned"
    children: Tuple["Column"] = ()
    sorting_order: Optional[List[str]] = None

def to_timestamp(d):
    result = int(pandas.to_datetime(d).timestamp()) * 1000
    # print(d, ":", result)
    return result

COLUMNS = [
    Column(
        header_name="Instrument Name",
        field="instrument_name",
        width=180,
    ),
    Column(
        header_name="Option",
        field="option_type",
        width=80,
    ),
    Column(header_name="Strike", field="strike", width=80),
    Column(
        header_name="Expiration",
        field="expiration_timestamp",
        formatter=js("dateFormatter"),
        sorting_order=["desc"],
    ),
    Column(header_name="Tick", field="tick_size", width=70),
    Column(
        header_name="Settlement Period",
        field="settlement_period",
        width=90,
    ),
    Column(
        header_name="Currency",
        field="quote_currency",
        width=80,
    ),
    Column(
        header_name="Min Trade Amount",
        field="min_trade_amount",
        width=80,
    ),
    Column(header_name="Kind", field="kind", width=70),
    Column(
        header_name="Active",
        field="is_active",
        preprocess=lambda x:x=="true",
        width=70,
    ),
    Column(
        header_name="Creation",
        field="creation_timestamp",
        formatter=js("dateFormatter"),
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
    Column(
        header_name="Currency",
        field="base_currency",
    ),
    Column(
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
