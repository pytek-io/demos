import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        antd.Descriptions(
            [
                antd.Descriptions.Item("Cloud Database", label="Product"),
                antd.Descriptions.Item("Prepaid", label="Billing"),
                antd.Descriptions.Item("18:00:00", label="time"),
                antd.Descriptions.Item("$80.00", label="Amount"),
                antd.Descriptions.Item("$20.00", label="Discount"),
                antd.Descriptions.Item("$60.00", label="Official"),
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
                    ],
                    label="Config Info",
                ),
            ],
            title="Responsive Descriptions",
            bordered=True,
            column={"xxl": 4, "xl": 3, "lg": 3, "md": 3, "sm": 2, "xs": 1},
        )
    )
