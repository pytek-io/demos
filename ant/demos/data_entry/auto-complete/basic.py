import random

import reflect as r
import reflect_antd as antd
import reflect_html as html


def mockVal(string: str):
    return (
        string
        + "".join(chr(random.randrange(97, 97 + 26)) for _ in range(10 - len(string))),
    )


def app():
    options = r.create_observable([])

    def onSearch(searchText: str):
        options.extend(
            [{"value": mockVal(searchText), "key": i} for i in range(10)]
            if searchText
            else []
        )

    def onSelect(data: str):
        print("onSelect", data)

    result = antd.AutoComplete(
        options=options,
        style=dict(width=200),
        onSelect=r.Callback(onSelect),
        onSearch=r.Callback(onSearch),
        placeholder="input here",
    )
    r.autorun(lambda: print("value", result()))
    return result
