import render as r
import render_antd as antd

# In the fifth row, other columns are merged into first column
# by setting it's colSpan to be 0
col_one = r.js_arrow("col_one", "(_, index) => index === 1 ? { colSpan: 0 } : {}")
render_name = r.js_arrow("render_name", "(_, index) => {colSpan: index === 1 ? 5 :1}")
render_phone_number = r.js_arrow(
    "render_phone_number",
    """
    (_, index) => {
      if (index === 3) {
        return { rowSpan: 2 };
      }
      // These two are merged into above cell
      if (index === 4) {
        return { rowSpan: 0 };
      }
      if (index === 1) {
        return { colSpan: 0 };
      }
      return {};
    }""",
)
data = [
    {
        "key": "1",
        "name": "John Brown",
        "age": 32,
        "tel": "0571-22098909",
        "phone": 18889898989,
        "address": "New York No. 1 Lake Park",
    },
    {
        "key": "2",
        "name": "Jim Green",
        "tel": "0571-22098333",
        "phone": 18889898888,
        "age": 42,
        "address": "London No. 1 Lake Park",
    },
    {
        "key": "3",
        "name": "Joe Black",
        "age": 32,
        "tel": "0575-22098909",
        "phone": 18900010002,
        "address": "Sidney No. 1 Lake Park",
    },
    {
        "key": "4",
        "name": "Jim Red",
        "age": 18,
        "tel": "0575-22098909",
        "phone": 18900010002,
        "address": "London No. 2 Lake Park",
    },
    {
        "key": "5",
        "name": "Jake White",
        "age": 18,
        "tel": "0575-22098909",
        "phone": 18900010002,
        "address": "Dublin No. 2 Lake Park",
    },
]

columns = [
    {"title": "Name", "dataIndex": "name", "onCell": render_name},
    {"title": "Age", "dataIndex": "age", "onCell": col_one},
    {
        "title": "Home phone",
        "colSpan": 2,
        "dataIndex": "tel",
        "onCell": render_phone_number,
    },
    {"title": "Phone", "colSpan": 0, "dataIndex": "phone", "onCell": col_one},
    {"title": "Address", "dataIndex": "address", "onCell": col_one},
]


def app(_):
    return antd.Table(columns=columns, dataSource=data, bordered=True)
