import json

import httpx
import reflect as r
import reflect_antd as antd
import reflect_html as html

IMAGE_STYLE = {
    "width": "20px",
    "height": "20px",
    "marginRight": 8,
    "verticalAlign": "middle",
}


def app():
    loading = r.ObservableValue(False)
    options = r.ObservableList([])

    async def onSearch(content, _prefix):
        if len(content) < 3:
            return
        loading.set(True)
        async with httpx.AsyncClient() as client:
            data = await client.get(
                f"https://api.github.com/search/users?q={content}"
            )
        options.set([
            {
                "label": [
                    html.img(src=record["avatar_url"], style=IMAGE_STYLE),
                    html.span(record["login"], style={"lineHeight": "22px"}),
                ],
                "value": str(record["login"]),
                "key": str(record["id"]),
            }
            for record in json.load(data)["items"]
        ])
        loading.set(False)

    return antd.Mentions(
        options=options,
        style={"width": "100%"},
        loading=loading,
        onSearch=onSearch,
    )
