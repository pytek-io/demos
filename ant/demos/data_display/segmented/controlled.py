import reflect as r
import reflect_antd as antd


def app():
    result = antd.Segmented(defaultValue="Map", options=["Map", "Transit", "Satellite"])
    r.autoprint(result)
    return result
