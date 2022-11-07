import reflect_antd as antd
import reflect_html as html

Option = antd.Mentions.Option


def app():
    return antd.Mentions(
        [
            Option("afc163", value="afc163"),
            Option("zombieJ", value="zombieJ"),
            Option("yesmeck", value="yesmeck"),
        ],
        style=dict(width="100%"),
        placement="top",
    )
