import render as r
import render_antd as antd


def app(_):
    result = antd.Segmented(defaultValue="Map", options=["Map", "Transit", "Satellite"])
    r.autoprint(result)
    return result
