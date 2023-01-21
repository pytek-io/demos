import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Slider(range={"draggableTrack": True}, defaultValue=[20, 50])
