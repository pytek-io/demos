from reflect_html import *
from reflect_antd import Descriptions, Badge


def app():
    return Descriptions(
        [
            Descriptions.Item("Cloud Database", label="Product"),
            Descriptions.Item("Prepaid", label="Billing Mode"),
            Descriptions.Item("YES", label="Automatic Renewal"),
            Descriptions.Item("2018-04-24 18:00:00", label="Order time"),
            Descriptions.Item("2019-04-24 18:00:00", label="Usage Time", span=2),
            Descriptions.Item(
                Badge(status="processing", text="Running"), label="Status", span=3
            ),
            Descriptions.Item("$80.00", label="Negotiated Amount"),
            Descriptions.Item("$20.00", label="Discount"),
            Descriptions.Item("$60.00", label="Official Receipts"),
            Descriptions.Item(
                [
                    "Data disk type: MongoDB",
                    br(),
                    "Database version: 3.4",
                    br(),
                    "Package: dds.mongo.mid",
                    br(),
                    "Storage space: 10 GB",
                    br(),
                    "Replication factor: 3",
                    br(),
                    "Region: East China 1",
                    br(),
                ],
                label="Config Info",
            ),
        ],
        title="User Info",
        bordered=True,
    )
