import render_antd as antd
import render_html as html


def app(_):
    return antd.Descriptions(
        [
            antd.Descriptions.Item(
                "Cloud Database",
                label="Product",
                labelStyle=labelStyle,
                contentStyle=contentStyle,
            ),
            antd.Descriptions.Item("Prepaid", label="Billing Mode"),
            antd.Descriptions.Item("YES", label="Automatic Renewal"),
        ],
        title="User Info",
        bordered=bordered,
    )


def app(_):
    return antd.Descriptions(
        [
            antd.Descriptions.Item("Cloud Database", label="Product"),
            antd.Descriptions.Item("Prepaid", label="Billing Mode"),
            antd.Descriptions.Item(
                "YES",
                label="Automatic Renewal",
                labelStyle={"color": "orange"},
                contentStyle={"color": "blue"},
            ),
        ],
        title="Root style",
        labelStyle=labelStyle,
        contentStyle=contentStyle,
        bordered=bordered,
    )


def app(_):
    return antd.Divider()
