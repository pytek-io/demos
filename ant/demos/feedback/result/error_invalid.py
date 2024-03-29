from render_ant_icons import CloseCircleOutlined
from render_antd import Button, Result, Typography
from render_html import *

Paragraph, Text = Typography.Paragraph, Typography.Text


def app(_):
    return [
        Result(
            "Go Console",
            status="error",
            title="Submission Failed",
            subTitle="Please check and modify the following information before resubmitting.",
            extra=[
                Button(type="primary", key="console"),
                Button("Buy Again", key="buy"),
                div(
                    [
                        Paragraph(
                            Text(
                                "The content you submitted has the following error:",
                                strong=True,
                                style=dict(fontSize=16),
                            )
                        ),
                        Paragraph(
                            [
                                CloseCircleOutlined(
                                    className="site-result-demo-error-icon"
                                ),
                                "Your account has been frozen.",
                                a("Thaw immediately >"),
                            ]
                        ),
                        Paragraph(
                            [
                                CloseCircleOutlined(
                                    className="site-result-demo-error-icon"
                                ),
                                "Your account is not yet eligible to apply.",
                                a("Apply Unlock >"),
                            ]
                        ),
                    ],
                    className="desc",
                ),
            ],
        )
    ]
