from reflect_html import *
from reflect_antd import AutoComplete, Input
from reflect import make_observable, autorun
from reflect import Callback

TextArea = Input.TextArea


def app():

    options = make_observable([])

    def handleSearch(value: str):
        options.extend(
            [
                {"value": None},
                {"value": value + value},
                {"value": value + value + value},
            ]
            if value
            else []
        )

    def handleKeyPress():
        print("handleKeyPress")

    def onSelect(value: str):
        print("onSelect", value)

    text_area = TextArea(
        placeholder="input here",
        className="custom",
        style=dict(height=50),
        onKeyPress=handleKeyPress,
    )
    result = AutoComplete(
        text_area,
        options=options,
        style=dict(width=200),
        onSelect=Callback(onSelect),
        onSearch=Callback(handleSearch),
    )
    autorun(lambda: print(result()))
    return result