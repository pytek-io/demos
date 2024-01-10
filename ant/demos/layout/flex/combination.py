import render_antd as antd
import render_html as html

cardStyle = {"width": 620}
imgStyle = {"display": "block", "width": 273}


def app(_):
    return antd.Card(
        [
            antd.Flex(
                [
                    html.img(
                        alt="avatar",
                        src="https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png",
                        style=imgStyle,
                    ),
                    antd.Flex(
                        [
                            antd.Typography.Title(
                                "antd is an enterprise-class UI design language and React UI library.",
                                level=3,
                            ),
                        ]
                    ),
                    antd.Button(
                        "Get Started",
                        href="https://ant.design",
                        type="primary",
                        target="_blank",
                    ),
                ],
                justify="space-between",
            ),
        ]
    )
