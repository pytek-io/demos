import render as r
import render_antd as antd


def app(_):
    check_box_group = antd.Checkbox.Group(
        antd.Row(
            [
                antd.Col(antd.Checkbox("A", key="A"), span=8),
                antd.Col(antd.Checkbox("B", key="B"), span=8),
                antd.Col(antd.Checkbox("C", key="C"), span=8),
                antd.Col(antd.Checkbox("D", key="D"), span=8),
                antd.Col(antd.Checkbox("E", key="E"), span=8),
            ]
        ),
        style={"width": "100%"},
    )
    r.autorun(lambda: print("checked = ", check_box_group()))
    return check_box_group
