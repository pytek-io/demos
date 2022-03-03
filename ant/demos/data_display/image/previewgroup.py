from reflect_html import *
from reflect_antd import Image


def app():
    return Image.PreviewGroup(
        [
            Image(
                width=200,
                src="https://gw.alipayobjects.com/zos/rmsportal/KDpgvguMpGfqaHPjicRK.svg",
            ),
            Image(
                width=200,
                src="https://gw.alipayobjects.com/zos/antfincdn/aPkFc8Sj7n/method-draw-image.svg",
            ),
        ]
    )
