import render as r
import render_antd as antd
import render_html as html

Paragraph, Text = antd.Typography.Paragraph, antd.Typography.Text


def app():
    ellipsis = antd.Switch(defaultChecked=True)
    return html.div(
        [
            ellipsis,
            Paragraph(
                "Ant Design, a design language for background applications, is refined by Ant UED Team. Ant Design, a design language for background applications, is refined by Ant UED Team. Ant Design, a design language for background applications, is refined by Ant UED Team. Ant Design, a design language for background applications, is refined by Ant UED Team. Ant Design, a design language for background applications, is refined by Ant UED Team. Ant Design, a design language for background applications, is refined by Ant UED Team.",
                ellipsis=ellipsis,
            ),
            Paragraph(
                "Ant Design, a design language for background applications, is refined by Ant UED Team. Ant Design, a design language for background applications, is refined by Ant UED Team. Ant Design, a design language for background applications, is refined by Ant UED Team. Ant Design, a design language for background applications, is refined by Ant UED Team. Ant Design, a design language for background applications, is refined by Ant UED Team. Ant Design, a design language for background applications, is refined by Ant UED Team.",
                ellipsis=lambda: {"rows": 2, "expandable": True, "symbol": "more"}
                if ellipsis()
                else False,
            ),
            Text(
                "Ant Design, a design language for background applications, is refined by Ant UED Team.",
                style=lambda: {"width": 100} if ellipsis() else None,
                ellipsis=lambda: {"tooltip": "I am ellipsis now!"}
                if ellipsis()
                else False,
            ),
        ]
    )
