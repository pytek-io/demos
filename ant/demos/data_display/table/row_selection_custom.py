import render as r
import render_antd as antd
import render_html as html

columns = [
    {"title": "Name", "dataIndex": "name"},
    {"title": "Age", "dataIndex": "age"},
    {"title": "Address", "dataIndex": "address"},
]
data = [
    {"key": i, "name": f"Edward {i}", "age": 32, "address": f"London Park no. {i}"}
    for i in range(46)
]


def selectedRowKeys(keys):
    print("selected", keys)


def app(_):
    selected_row_keys = r.ObservableList([])

    def onChange(newSelectedRowKeys):
        print(f"selectedRowKeys: {newSelectedRowKeys}")
        selected_row_keys.set(newSelectedRowKeys)

    def select_keys(selector):
        return lambda selectable_keys: selected_row_keys.set(
            [key for key in selectable_keys if selector(key)]
        )

    def rowSelection():
        return antd.RowSelection(**{
            "selectedRowKeys": selected_row_keys(),
            "onChange": onChange,
            "selections": [
                antd.Table.SELECTION_ALL,
                antd.Table.SELECTION_INVERT,
                antd.Table.SELECTION_NONE,
                {
                    "key": "odd",
                    "text": "Odd rows",
                    "onSelect": select_keys(lambda x: x % 2 == 1),
                },
                {
                    "key": "even",
                    "text": "Even rows",
                    "onSelect": select_keys(lambda x: x % 2 == 0),
                },
            ],
            "type": shape(),
        })

    shape = antd.Radio.Group(
        [
            antd.Radio("Checkbox", value="checkbox"),
            antd.Radio("Radio", value="radio"),
        ]
    )
    return html.div(
        [
            shape,
            antd.Divider(),
            antd.Table(columns=columns, rowSelection=rowSelection, dataSource=data),
        ]
    )
