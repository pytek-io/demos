from render_antd import Button, Descriptions, Radio
from render_html import *


def app(_):
    return[
 div([Radio.Group([Radio("default", value="default"), Radio("middle", value="middle"), Radio("small", value="small")], onChange=this.onChange, value=this.state.size), br(), br(), Descriptions("Edit", bordered=True, title="Custom Size", size=this.state.size, extra="{Button(type=", primary"=True), "}"         >", Descriptions.Item("Cloud Database", label="Product"), Descriptions.Item("Prepaid", label="Billing"), Descriptions.Item("18:00:00", label="time"), Descriptions.Item("$80.00", label="Amount"), Descriptions.Item("$20.00", label="Discount"), Descriptions.Item("$60.00", label="Official"), Descriptions.Item(["Data disk type: MongoDB", br(), "Database version: 3.4", br(), "Package: dds.mongo.mid", br(), "Storage space: 10 GB", br(), "Replication factor: 3", br(), "Region: East China 1", br()], label="Config Info")]),
 br(),
 br(),
 Descriptions("Edit", title="Custom Size", size=this.state.size, extra="{<Button type=", primary"=True),
 Descriptions.Item("Cloud Database", label="Product"),
 Descriptions.Item("Prepaid", label="Billing"),
 Descriptions.Item("18:00:00", label="time"),
 Descriptions.Item("$80.00", label="Amount"),
 Descriptions.Item("$20.00", label="Discount"),
 Descriptions.Item("$60.00", label="Official"),
]
def app(_):
    return Demo()