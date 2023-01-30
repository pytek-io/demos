import reflect as r
import reflect_antd as antd

mockData = [{"key": i, "title": f"content{i + 1}"} for i in range(10)]

get_title = r.JSMethod("get_title", f"""return arg.title""", "arg")


def app():
    result = antd.Transfer(
        dataSource=mockData, titles=["Source", "Target"], render=get_title
    )
    r.autoprint(result)
    return result
