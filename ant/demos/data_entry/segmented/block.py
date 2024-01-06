import render_antd as antd


def app():
    return antd.Segmented(
        block=True, options=[123, 456, "longtext-longtext-longtext-longtext"]
    )
