import render as r
import render_antd as antd


def subtract_attributes(name):
    return r.js_arrow(f"subtract_{name}", f"(a, b) => a.{name} - b.{name}")


def compare_length(name):
    return r.js_arrow(
        f"compare_{name}_length", f"(a, b) => a.{name}.length - b.{name}.length"
    )


is_included = r.js_arrow("is_included", "(value, {name}) => name.indexOf(value) === 0")


def app(_):
    columns = [
        {
            "title": "Name",
            "dataIndex": "name",
            "filters": [
                {"text": "Joe", "value": "Joe"},
                {"text": "Jim", "value": "Jim"},
                # {
                #     "text": "Submenu",
                #     "value": "Submenu",
                #     "children": [
                #         {"text": "Green", "value": "Green"},
                #         {"text": "Black", "value": "Black"},
                #     ],
                # },
            ],
            "onFilter": is_included,
            "sorter": compare_length("name"),
            "sortDirections": ["descend"],
        },
        {
            "title": "Age",
            "dataIndex": "age",
            "defaultSortOrder": "descend",
            "sorter": subtract_attributes("age"),
        },
        {
            "title": "Address",
            "dataIndex": "address",
            "filters": [
                {"text": "London", "value": "London"},
                {"text": "New York", "value": "New York"},
            ],
            "filterMultiple": False,
            "onFilter": is_included,
            "sorter": compare_length("address"),
            "sortDirections": ["descend", "ascend"],
        },
    ]
    data = [
        {
            "key": "1",
            "name": "John Brown",
            "age": 32,
            "address": "New York No. 1 Lake Park",
        },
        {
            "key": "2",
            "name": "Jim Green",
            "age": 42,
            "address": "London No. 1 Lake Park",
        },
        {
            "key": "3",
            "name": "Joe Black",
            "age": 32,
            "address": "Sidney No. 1 Lake Park",
        },
        {"key": "4", "name": "Jim Red", "age": 32, "address": "London No. 2 Lake Park"},
    ]
    return antd.Table(
        columns=columns,
        dataSource=data,
        onChange=lambda x: print("params", x),
    )
