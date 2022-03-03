from reflect_html import *
from reflect_antd import Table
from reflect import js

columns = [
    {
        "title": "Name",
        "dataIndex": "name",
        "key": "name",
        "width": 100,
        "fixed": "left",
        "filters": [{"text": "Joe", "value": "Joe"}, {"text": "John", "value": "John"}],
        "onFilter": js("column_filter"),
    },
    {
        "title": "Other",
        "children": [
            {
                "title": "Age",
                "dataIndex": "age",
                "key": "age",
                "width": 150,
                "sorter": js("substract_attributes", "age"),
            },
            {
                "title": "Address",
                "children": [
                    {
                        "title": "Street",
                        "dataIndex": "street",
                        "key": "street",
                        "width": 150,
                    },
                    {
                        "title": "Block",
                        "children": [
                            {
                                "title": "Building",
                                "dataIndex": "building",
                                "key": "building",
                                "width": 100,
                            },
                            {
                                "title": "Door No.",
                                "dataIndex": "number",
                                "key": "number",
                                "width": 100,
                            },
                        ],
                    },
                ],
            },
        ],
    },
    {
        "title": "Company",
        "children": [
            {
                "title": "Company Address",
                "dataIndex": "companyAddress",
                "key": "companyAddress",
                "width": 200,
            },
            {"title": "Company Name", "dataIndex": "companyName", "key": "companyName"},
        ],
    },
    {
        "title": "Gender",
        "dataIndex": "gender",
        "key": "gender",
        "width": 80,
        "fixed": "right",
    },
]

data = [
    {
        "key": i,
        "name": "John Brown",
        "age": i + 1,
        "street": "Lake Park",
        "building": "C",
        "number": 2035,
        "companyAddress": "Lake Street 42",
        "companyName": "SoftLake Co",
        "gender": "M",
    }
    for i in range(100)
]


def app():
    return Table(
        columns=columns,
        dataSource=data,
        bordered=True,
        size="middle",
        scroll=dict(x="calc(700px + 50%)", y=240),
    )
