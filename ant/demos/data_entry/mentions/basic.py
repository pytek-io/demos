import reflect as r
import reflect_antd as antd
import reflect_html as html

Option = antd.Mentions.Option


def onSelect(value):
    print("selected", value)


def app():
    mentions = antd.Mentions(
        [
            Option("afc163", value="afc163"),
            Option("zombieJ", value="zombieJ"),
            Option("yesmeck", value="yesmeck"),
        ],
        style=dict(width="100%"),
        onSelect=r.Callback(onSelect),
        defaultValue="@afc163",
    )
    r.autorun(lambda: print(mentions()))
    return mentions
