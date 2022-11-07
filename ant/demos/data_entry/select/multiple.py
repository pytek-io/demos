import reflect as r
import reflect_antd as antd
import reflect_html as html

Option = antd.Select.Option


def app():
    children = [
        Option(key, key=key)
        for key in (f"{chr(i + ord('a'))}{i}" for i in range(10, 36))
    ]
    select1 = antd.Select(
        children,
        mode="multiple",
        allowClear=True,
        style=dict(width="100%"),
        placeholder="Please select",
        defaultValue=["a10", "c12"],
    )
    select2 = antd.Select(
        children,
        mode="multiple",
        disabled=True,
        style=dict(width="100%"),
        placeholder="Please select",
        defaultValue=["a10", "c12"],
    )
    r.autorun(lambda: print(select1()))
    r.autorun(lambda: print(select2()))
    return html.div([select1, html.br(), select2])
