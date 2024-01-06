import render_antd as antd


def app():
    return antd.Flex(
        [antd.Button("Button", type="primary") for i in range(24)],
        gap="small",
        wrap="wrap",
    )
