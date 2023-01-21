import reflect as r
import reflect_antd as antd

TextArea = antd.Input.TextArea
domains = ["gmail.com", "163.com", "qq.com"]


def app():
    options_obs = r.ObservableList()

    def handleSearch(value: str):
        options_obs.set(
            [
                {"value": f"{value}@{domain}"}
                for domain in ([] if "@" in value else domains)
            ]
        )

    result = antd.AutoComplete(
        options=options_obs, style={"width": 200}, onSearch=r.Callback(handleSearch)
    )
    r.autoprint(result)
    return result
