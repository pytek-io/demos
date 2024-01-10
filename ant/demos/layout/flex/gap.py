import render_antd as antd

baseStyle = {"width": "25%", "height": 54}


def app(_):
    gap = antd.Radio.Group(
        [
            antd.Radio(value, value=value) for value in ['small', 'middle', 'large', 'customize']
        ],
    )
    custom_gap = antd.Slider()
    return antd.Flex(
        [
            gap,
            lambda: custom_gap if gap() == 'customize' else None,
            antd.Flex(
                [antd.Button("Primary", type="primary") for i in range(4)],
                vertical=gap,
                gap=lambda: custom_gap() if gap() == 'customize' else gap(),
            ),
        ],
        gap="middle",
        vertical=True,
    )
