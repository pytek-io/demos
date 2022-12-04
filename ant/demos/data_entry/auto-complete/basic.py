import random

import reflect as r
import reflect_antd as antd


def mock_val(string: str):
    return string + "".join(
        chr(random.randrange(65, 65 + 26)) for _ in range(10 - len(string))
    )


def app():
    options = [{"value": mock_val("A")} for i in range(10)]
    options_obs = r.ObservableList(options.copy())

    def on_search(search_text: str):
        search_text = search_text.upper()
        filtered_options = (
            [element for element in options if search_text in element["value"]]
            if search_text
            else options
        )
        options_obs.set(filtered_options)

    result = antd.AutoComplete(
        defaultValue=options[0]["value"],
        options=options_obs,
        style={"width": 200},
        # onSearch=r.Callback(on_search),
        placeholder="input here",
        onChange=lambda x: x.upper() if x else x,
        allowClear=True,
        # filterOption=r.js("autoCompleteFilterOption"),
    )
    r.autoprint(result)
    return result
