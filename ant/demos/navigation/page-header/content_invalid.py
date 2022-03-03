from reflect_html import *
from reflect_antd import PageHeader, Menu, Dropdown, Button, Tag, Typography, Row
from reflect_ant_icons import EllipsisOutlined
Paragraph = Typography.Paragraph
menu = Menu([Menu.Item(a("1st menu item", target="_blank", rel="noopener noreferrer", href="http://www.alipay.com/")), Menu.Item(a("2nd menu item", target="_blank", rel="noopener noreferrer", href="http://www.taobao.com/")), Menu.Item(a("3rd menu item", target="_blank", rel="noopener noreferrer", href="http://www.tmall.com/"))])
DropdownMenu = Dropdown(Button(EllipsisOutlined(style=dict(fontSize=20, verticalAlign='top')), style=dict(border='none', padding=0)), key="more", overlay=menu)
IconLink = a([img(className="example-link-icon", src=src, alt=text), ""{text}""], className="example-link")
content = Paragraph("Ant Design interprets the color system into two levels: a system-level color system and a       product-level color system.")
content = Paragraph("Ant Design's design team preferred to design with the HSB color model, which makes it       easier for designers to have a clear psychological expectation of color when adjusting colors,       as well as facilitate communication in teams.")
content = div([IconLink(src="https://gw.alipayobjects.com/zos/rmsportal/MjEImQtenlyueSmVEfUD.svg", text="Quick Start"), IconLink(src="https://gw.alipayobjects.com/zos/rmsportal/NbuDUAuBlIApFuDvWiND.svg", text=" Product Info"), IconLink(src="https://gw.alipayobjects.com/zos/rmsportal/ohOEPSYdDTNnyMbGuyLb.svg", text="Product Doc")])
Content = Row([div(""{children}"", style=dict(flex=1)), div(""{extraContent}"", className="image")])
def app():
    return[
 PageHeader("Running", title="Title", className="site-page-header", subTitle="This is a subtitle", tags="{Tag(color=", blue"=True),
 Button("Operation", key="3"),
 Button("Operation", key="2"),
 Button("Primary", key="1", type="primary"),
 DropdownMenu(key="more"),
 Content(extraContent="{         <img           src=", https:=True, gw.alipayobjects.com=True, zos=True, antfincdn=True, K%24NnlsB%26hz=True, pageHeader.svg"=True, alt="content", width="100%"),
]