"""
Showing how options can be dynamically populated according to the user input.
"""
import render as r
import render_antd as antd


def app(_):
    options_obs = r.ObservableList()

    def on_search(search_text: str):
        filtered_options = []
        if search_text:
            search_text = search_text.upper()
            filtered_options = [{"value": search_text * i} for i in range(1, 4)]
        options_obs.set(filtered_options)

    result = antd.AutoComplete(
        defaultValue="",
        options=options_obs,
        style={"width": 200},
        onSearch=on_search,
        placeholder="input here",
        onChange=lambda x: x.upper() if x else x,
        allowClear=True,
    )
    r.autoprint(result)
    return result
