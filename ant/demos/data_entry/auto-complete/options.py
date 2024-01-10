import render as r
import render_antd as antd

TextArea = antd.Input.TextArea
domains = ["gmail.com", "163.com", "qq.com"]


def app(_):
    options_obs = r.ObservableList()

    def handleSearch(value: str):
        options_obs.set(
            [
                {"value": f"{value}@{domain}"}
                for domain in ([] if "@" in value else domains)
            ]
        )

    result = antd.AutoComplete(
        options=options_obs, style={"width": 200}, onSearch=handleSearch
    )
    r.autoprint(result)
    return result
