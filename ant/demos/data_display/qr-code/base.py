import render_antd as antd


def app(_):
    text_input = antd.Input(placeholder="https://pytek.io", maxLength=60)
    return antd.Space(
        [antd.QRCode(value=text_input, size=200), text_input],
        direction="vertical",
        align="center",
    )
