import render_antd as antd
import render_html as html

columns = [
    {"title": "Name", "dataIndex": "name", "width": 150},
    {"title": "Age", "dataIndex": "age", "width": 150},
    {"title": "Address", "dataIndex": "address"},
]
data = [
    {"key": i, "name": f"Edward {i}", "age": 32, "address": f"London Park no. {i}"}
    for i in range(100)
]


def app():
    return antd.Table(
        columns=columns, dataSource=data, pagination={"pageSize": 50}, scroll={"y": 240}
    )
