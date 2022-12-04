import reflect as r
import reflect_antd as antd
import reflect_html as html

columns = [
    {"title": "Name", "dataIndex": "name"},
    {
        "title": "Chinese Score",
        "dataIndex": "chinese",
        "sorter": {"compare": r.js("substract_attributes", "chinese"), "multiple": 3},
    },
    {
        "title": "Math Score",
        "dataIndex": "math",
        "sorter": {"compare": r.js("substract_attributes", "math"), "multiple": 2},
    },
    {
        "title": "English Score",
        "dataIndex": "english",
        "sorter": {"compare": r.js("substract_attributes", "english"), "multiple": 1},
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
        onChange=r.Callback(lambda x: print("params", x)),
    )
