from render_ant_icons import createFromIconfontCN
from render_html import *


def app(_):
    return div(
        [
            IconFont(type="icon-javascript"),
            IconFont(type="icon-java"),
            IconFont(type="icon-shoppingcart"),
            IconFont(type="icon-python"),
        ],
        className="icons-list",
    )
