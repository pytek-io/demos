from render_ant_icons import HighlightOutlined, SmileFilled, SmileOutlined
from render_antd import Typography
from render_html import *

Paragraph = Typography.Paragraph
def app():
    return[
 Paragraph(""{editableStr}"", editable=dict(onChange=setEditableStr)),
 Paragraph(""{customIconStr}"", editable=dict(icon=<HighlightOutlined />, tooltip='click to edit text', onChange=setCustomIconStr)),
 Paragraph(""{hideTooltipStr}"", editable=dict(tooltip=false, onChange=setHideTooltipStr)),
 Paragraph(""{lengthLimitedStr}"", editable="{!           onChange: setLengthLimitedStr,           maxLength: 50,           autoSize: ", {=True, maxRows:=True, 5,=True, minRows:=True, 3=True, }",=True, !}"=True),
 Paragraph("This is a copyable text.", copyable=True),
 Paragraph("Replace copy text.", copyable=dict(text='Hello)),
 Paragraph(copyable="{!           icon: [<SmileOutlined key=", copy-icon"=True),
 SmileFilled(key="copied-icon"),
 Paragraph("Hide Copy tooltips.", copyable=dict(tooltips=false)),
]
def app():
    return Demo()