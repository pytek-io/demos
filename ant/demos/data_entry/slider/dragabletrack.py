import render_antd as antd
import render_html as html


def app():
    return antd.Slider(range={"draggableTrack": True}, defaultValue=[20, 50])
