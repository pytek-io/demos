from reflect_html import *
from reflect_antd import Descriptions


def app():
    return div(
        Descriptions(
            [
                Descriptions.Item("Cloud Database", label="Product"),
                Descriptions.Item("Prepaid", label="Billing"),
                Descriptions.Item("18:00:00", label="time"),
                Descriptions.Item("$80.00", label="Amount"),
                Descriptions.Item("$20.00", label="Discount"),
                Descriptions.Item("$60.00", label="Official"),
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
                    ],
                    label="Config Info",
                ),
            ],
            title="Responsive Descriptions",
            bordered=True,
            column=dict(xxl=4, xl=3, lg=3, md=3, sm=2, xs=1),
        )
    )
