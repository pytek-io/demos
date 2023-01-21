import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    children = [
        {"label": key, "key": key}
        for key in (f"{chr(i + ord('a'))}{i}" for i in range(10, 36))
    ]
    select1 = antd.Select(
        options=children,
        mode="multiple",
        allowClear=True,
        style={"width": "100%"},
        placeholder="Please select",
        defaultValue=["a10", "c12"],
    )
    select2 = antd.Select(
        options=children,
        mode="multiple",
        disabled=True,
        style={"width": "100%"},
        placeholder="Please select",
        defaultValue=["a10", "c12"],
    )
    r.autorun(lambda: print(select1()))
    r.autorun(lambda: print(select2()))
    return html.div([select1, html.br(), select2])
