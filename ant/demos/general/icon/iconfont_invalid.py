from render_html import *
from render_ant_icons import createFromIconfontCN


IconFont = createFromIconfontCN({
  "scriptUrl": '//at.alicdn.com/t/font_8d5l8fzk5b87iudi.js',
})

def app():
    return [
        div(
            [
                IconFont(type="icon-tuichu"),
                IconFont(type="icon-facebook"),
                IconFont(type="icon-twitter"),
            ],
            className="icons-list",
        ),
    ]
