import render_antd as antd
import render_html as html


def app(_):
    return antd.Skeleton(avatar=True, paragraph={"rows": 4})
