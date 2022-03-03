from reflect_html import *
from reflect_antd import Descriptions, Divider


def app():
    return Descriptions(
        [
            Descriptions.Item(
                "Cloud Database",
                label="Product",
                labelStyle=labelStyle,
                contentStyle=contentStyle,
            ),
            Descriptions.Item("Prepaid", label="Billing Mode"),
            Descriptions.Item("YES", label="Automatic Renewal"),
        ],
        title="User Info",
        bordered=bordered,
    )


def app():
    return Descriptions(
        [
            Descriptions.Item("Cloud Database", label="Product"),
            Descriptions.Item("Prepaid", label="Billing Mode"),
            Descriptions.Item(
                "YES",
                label="Automatic Renewal",
                labelStyle=dict(color="orange"),
                contentStyle=dict(color="blue"),
            ),
        ],
        title="Root style",
        labelStyle=labelStyle,
        contentStyle=contentStyle,
        bordered=bordered,
    )


def app():
    return Divider()
