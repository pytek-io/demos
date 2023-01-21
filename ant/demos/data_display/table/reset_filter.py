from reflect_antd import Button, Space, Table
from reflect_html import *


def app():
    columns = [
        {
            "title": "Name",
            "dataIndex": "name",
            "filters": [
                {"text": "Joe", "value": "Joe"},
                {"text": "Jim", "value": "Jim"},
                {
                    "text": "Submenu",
                    "value": "Submenu",
                    "children": [
                        {"text": "Green", "value": "Green"},
                        {"text": "Black", "value": "Black"},
                    ],
                },
            ],
            "onFilter": js("column_filter"),
            "sorter": js("substract_attributes", "name.length"),
            "sortDirections": ["descend"],
        },
        {
            "title": "Age",
            "dataIndex": "age",
            "defaultSortOrder": "descend",
            "sorter": js("substract_attributes", "age"),
        },
        {
            "title": "Address",
            "dataIndex": "address",
            "filters": [
                {"text": "London", "value": "London"},
                {"text": "New York", "value": "New York"},
            ],
            "filterMultiple": False,
            "onFilter": js("column_filter"),
            "sorter": js("substract_attributes", "address.length"),
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
    return [
        Space(
            [
                Button("Sort age", onClick=this.setAgeSort),
                Button("Clear filters", onClick=this.clearFilters),
                Button("Clear filters and sorters", onClick=this.clearAll),
            ],
            style={"marginBottom": 16},
        ),
        Table(columns=columns, dataSource=data, onChange=this.handleChange),
    ]
