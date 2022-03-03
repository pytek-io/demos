from reflect_html import *
from reflect_antd import Space, Button


def app():
    return Space(
        # eslint-disable-next-line react/no-array-index-key"
        [Button("Button", key=index) for index in range(20)],
        size=[8, 16],
        wrap=True,
    )
