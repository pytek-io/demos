from reflect import autorun, js
from reflect_antd import Transfer

mockData = [{"key": i, "title": f"content{i + 1}"} for i in range(10)]


def app():
    result = Transfer(
        dataSource=mockData,
        titles=["Source", "Target"],
        defaultTargetKeys=[item["key"] for item in mockData if item["key"] % 2 == 0],
        render=js("fetch_attribute", "title"),
    )
    autorun(lambda: print("target", result()))
    return result
