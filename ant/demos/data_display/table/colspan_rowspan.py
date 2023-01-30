import reflect as r
import reflect_antd as antd

# In the fifth row, other columns are merged into first column
# by setting it's colSpan to be 0
shared_on_cell = r.JSMethod(
    "shared_on_cell", "return index === 1 ? { colSpan: 0 } : {};", "_", "index"
)
render_name = r.JSMethod(
    "render_name", "return  { colSpan: index === 1 ? 5 :1 };", "_", "index"
)

render_phone_number = r.JSMethod(
    "render_phone_number",
    """
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
""",
    "_",
    "index",
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
    {"title": "Age", "dataIndex": "age", "onCell": shared_on_cell},
    {
        "title": "Home phone",
        "colSpan": 2,
        "dataIndex": "tel",
        "onCell": render_phone_number,
    },
    {"title": "Phone", "colSpan": 0, "dataIndex": "phone", "onCell": shared_on_cell},
    {"title": "Address", "dataIndex": "address", "onCell": shared_on_cell},
]


def app():
    return antd.Table(columns=columns, dataSource=data, bordered=True)
