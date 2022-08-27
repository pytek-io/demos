from reflect_html import *
from reflect_antd import Typography, Switch
from reflect import create_observable

Paragraph, Text = Typography.Paragraph, Typography.Text


def app():
    ellipsis = Switch(defaultChecked=True)
    return [
        ellipsis,
        Paragraph(
            "Ant Design, a design language for background applications, is refined by Ant UED Team. Ant Design, a design language for background applications, is refined by Ant UED Team. Ant Design, a design language for background applications, is refined by Ant UED Team. Ant Design, a design language for background applications, is refined by Ant UED Team. Ant Design, a design language for background applications, is refined by Ant UED Team. Ant Design, a design language for background applications, is refined by Ant UED Team.",
            ellipsis=ellipsis,
        ),
        Paragraph(
            "Ant Design, a design language for background applications, is refined by Ant UED Team. Ant Design, a design language for background applications, is refined by Ant UED Team. Ant Design, a design language for background applications, is refined by Ant UED Team. Ant Design, a design language for background applications, is refined by Ant UED Team. Ant Design, a design language for background applications, is refined by Ant UED Team. Ant Design, a design language for background applications, is refined by Ant UED Team.",
            ellipsis=lambda: (
                {"rows": 2, "expandable": True, "symbol": "more"}
                if ellipsis()
                else False
            ),
        ),
        Text(
            "Ant Design, a design language for background applications, is refined by Ant UED Team.",
            style=lambda: {"width": 100} if ellipsis() else None,
            ellipsis=lambda: {"tooltip": "I am ellipsis now!"} if ellipsis() else False,
        ),
    ]
