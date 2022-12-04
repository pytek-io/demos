import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Tag("Twitter", icon=ant_icons.TwitterOutlined([]), color="#55acee"),
            antd.Tag("Youtube", icon=ant_icons.YoutubeOutlined([]), color="#cd201f"),
            antd.Tag("Facebook", icon=ant_icons.FacebookOutlined([]), color="#3b5999"),
            antd.Tag("LinkedIn", icon=ant_icons.LinkedinOutlined([]), color="#55acee"),
        ]
    )
