from reflect_html import *
from reflect_antd import BackTop


def app():
    return div([BackTop(), strong("gray", className="site-back-top-basic")])
