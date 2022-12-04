import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Descriptions(
        [
            antd.Descriptions.Item("Cloud Database", label="Product"),
            antd.Descriptions.Item("Prepaid", label="Billing Mode"),
            antd.Descriptions.Item("YES", label="Automatic Renewal"),
            antd.Descriptions.Item("2018-04-24 18:00:00", label="Order time"),
            antd.Descriptions.Item("2019-04-24 18:00:00", label="Usage Time", span=2),
            antd.Descriptions.Item(
                antd.Badge(status="processing", text="Running"), label="Status", span=3
            ),
            antd.Descriptions.Item("$80.00", label="Negotiated Amount"),
            antd.Descriptions.Item("$20.00", label="Discount"),
            antd.Descriptions.Item("$60.00", label="Official Receipts"),
            antd.Descriptions.Item(
                [
                    "Data disk type: MongoDB",
                    html.br(),
                    "Database version: 3.4",
                    html.br(),
                    "Package: dds.mongo.mid",
                    html.br(),
                    "Storage space: 10 GB",
                    html.br(),
                    "Replication factor: 3",
                    html.br(),
                    "Region: East China 1",
                    html.br(),
                ],
                label="Config Info",
            ),
        ],
        title="User Info",
        bordered=True,
    )
