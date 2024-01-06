import render_antd as antd


def app():
    return antd.Space(
        [
            antd.QRCode(value="https://pytek.io", size=200, color="green"),
            antd.QRCode(
                value="https://pytek.io", size=200, color="blue", bgColor="yellow"
            ),
        ],
        direction="vertical",
        align="center",
    )
