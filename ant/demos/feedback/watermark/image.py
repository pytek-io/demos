import render_antd as antd
import render_html as html


def app(_):
    return antd.Watermark(
        html.div("Ant Design"),
        image="https://mdn.alipayobjects.com/huamei_7uahnr/afts/img/A*lkAoRbywo0oAAAAAAAAAAAAADrJ8AQ/original",
        style={"height": 130, "width": 130},
    )
