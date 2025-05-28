import render as r
import render_antd as antd

mockData = [{"key": i, "title": f"content{i + 1}"} for i in range(10)]

get_title = r.js_arrow("get_title", "({title}) => title")


def app(_):
    targetKeys=r.ObservableList([1, 2, 3])
    result = antd.Transfer(
        dataSource=mockData, titles=["Source", "Target"], render=get_title,
        # selectedKeys=[0, 1, 2],
        targetKeys=targetKeys,
        )
    r.autoprint(targetKeys)
    return result
