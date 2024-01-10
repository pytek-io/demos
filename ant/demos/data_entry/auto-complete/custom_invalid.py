import render as r
import render_antd as antd

TextArea = antd.Input.TextArea


def app(_):
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
    r.autoprint(result)
    return result
