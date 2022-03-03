from reflect_html import *
from reflect_antd import Slider


def app():
    return Slider(range=dict(draggableTrack=True), defaultValue=[20, 50])
