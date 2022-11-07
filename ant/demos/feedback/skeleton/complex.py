import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Skeleton(avatar=True, paragraph=dict(rows=4))
