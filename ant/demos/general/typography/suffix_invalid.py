from reflect_html import *
from reflect_antd import Typography, Slider
Paragraph = Typography.Paragraph
rows = this.rows
def app():
    return[
 Slider(value=rows, min=1, max=10, onChange=this.onChange),
 Paragraph(""{article}"", ellipsis="{!             rows,             expandable: true,             suffix: '--William Shakespeare',             onEllipsis: ellipsis => ", {=True, print('Ellipsis=True, changed:',=True, ellipsis);=True, }",=True, !}"=True, title="{`$", {article}"--William=True, Shakespeare`}"=True),
]
def app():
    return Demo()