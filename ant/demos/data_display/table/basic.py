import reflect as r
import reflect_antd as antd


def app():
    columns = [
        {"title": "Name", "dataIndex": "name", "key": "name"},
        {"title": "Age", "dataIndex": "age", "key": "age"},
        {"title": "Address", "dataIndex": "address", "key": "address"},
        {"title": "Tags", "key": "tags", "dataIndex": "tags"},
        {"title": "Action", "key": "action"},
    ]
    data = [
        {
            "key": "1",
            "name": "John Brown",
            "age": 32,
            "address": "New York No. 1 Lake Park",
            "tags": ["nice", "developer"],
        },
        {
            "key": "2",
            "name": "Jim Green",
            "age": 42,
            "address": "London No. 1 Lake Park",
            "tags": ["winner"],
        },
        {
            "key": "3",
            "name": "Joe Black",
            "age": 32,
            "address": "Sidney No. 1 Lake Park",
            "tags": ["cool", "teacher"],
        },
    ]
    return antd.Table(columns=columns, dataSource=data)
