from itertools import count

import render as r
import render_antd as antd


def subtract_attributes(name):
    return r.js_arrow(f"subtract_{name}", f"(a, b) => a.{name} - b.{name}")


is_included = r.js_arrow("is_included", "(value, {name}) => name.indexOf(value) === 0")


columns = [
    {
        "title": "Name",
        "dataIndex": "name",
        "key": "name",
        "width": 100,
        "fixed": "left",
        "filters": [{"text": "Joe", "value": "Joe"}, {"text": "John", "value": "John"}],
        "onFilter": is_included,
    },
    {
        "title": "Other",
        "children": [
            {
                "title": "Age",
                "dataIndex": "age",
                "key": "age",
                "width": 150,
                "sorter": subtract_attributes("age"),
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
data = []
key = count()
for i in range(10):
    for name in ["John Brown", "Joe Black"]:
        data.append(
            {
                "key": next(key),
                "name": name,
                "age": i + 1,
                "street": "Lake Park",
                "building": "C",
                "number": 2035,
                "companyAddress": "Lake Street 42",
                "companyName": "SoftLake Co",
                "gender": "M",
            }
        )


def app():
    return antd.Table(
        columns=columns,
        dataSource=data,
        bordered=True,
        size="middle",
        scroll={"x": "calc(700px + 50%)", "y": 240},
    )
