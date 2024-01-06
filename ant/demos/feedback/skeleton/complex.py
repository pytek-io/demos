import render_antd as antd
import render_html as html


def app():
    return antd.Skeleton(avatar=True, paragraph={"rows": 4})
