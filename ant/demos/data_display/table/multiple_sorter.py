import render as r
import render_antd as antd


def subtract_attributes(name):
    return r.js_arrow(f"subtract_{name}", f"(a, b) => a.{name} - b.{name}")


columns = [
    {"title": "Name", "dataIndex": "name"},
    {
        "title": "Chinese Score",
        "dataIndex": "chinese",
        "sorter": {"compare": subtract_attributes("chinese"), "multiple": 3},
    },
    {
        "title": "Math Score",
        "dataIndex": "math",
        "sorter": {"compare": subtract_attributes("math"), "multiple": 2},
    },
    {
        "title": "English Score",
        "dataIndex": "english",
        "sorter": {"compare": subtract_attributes("english"), "multiple": 1},
    },
]
data = [
    {"key": "1", "name": "John Brown", "chinese": 98, "math": 60, "english": 70},
    {"key": "2", "name": "Jim Green", "chinese": 98, "math": 66, "english": 89},
    {"key": "3", "name": "Joe Black", "chinese": 98, "math": 90, "english": 70},
    {"key": "4", "name": "Jim Red", "chinese": 88, "math": 99, "english": 89},
]


def app():
    return antd.Table(
        columns=columns,
        dataSource=data,
        onChange=lambda x: print("params", x),
    )
