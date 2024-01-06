import render_antd as antd
import render_html as html


def app():
    return antd.Image.PreviewGroup(
        [
            antd.Image(
                width=200,
                src="https://gw.alipayobjects.com/zos/rmsportal/KDpgvguMpGfqaHPjicRK.svg",
            ),
            antd.Image(
                width=200,
                src="https://gw.alipayobjects.com/zos/antfincdn/aPkFc8Sj7n/method-draw-image.svg",
            ),
        ]
    )
