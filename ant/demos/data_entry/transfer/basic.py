import reflect as r
import reflect_antd as antd

mockData = [{"key": i, "title": f"content{i + 1}"} for i in range(10)]


def app():
    result = antd.Transfer(
        dataSource=mockData,
        titles=["Source", "Target"],
        render=r.js("fetch_attribute", "title"),
    )
    r.autorun(lambda: print("target", result()))
    return result
