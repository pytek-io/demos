from reflect_html import *
from reflect_antd import AutoComplete
from reflect import Callback
from reflect import make_observable, autorun
from random import randrange


def mockVal(string: str):
    return (
        string + "".join(chr(randrange(97, 97 + 26)) for _ in range(10 - len(string))),
    )


def app():
    options = make_observable([])

    def onSearch(searchText: str):
        options.extend(
            [{"value": mockVal(searchText), "key": i} for i in range(10)]
            if searchText
            else []
        )

    def onSelect(data: str):
        print("onSelect", data)

    result = AutoComplete(
        options=options,
        style=dict(width=200),
        onSelect=Callback(onSelect),
        onSearch=Callback(onSearch),
        placeholder="input here",
    )
    autorun(lambda: print("value", result()))
    return result