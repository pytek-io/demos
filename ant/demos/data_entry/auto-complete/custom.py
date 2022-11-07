import reflect as r
import reflect_antd as antd
import reflect_html as html

TextArea = antd.Input.TextArea


def app():
    options = r.create_observable([])

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
    result = antd.AutoComplete(
        text_area,
        options=options,
        style=dict(width=200),
        onSelect=r.Callback(onSelect),
        onSearch=r.Callback(handleSearch),
    )
    r.autorun(lambda: print(result()))
    return result
