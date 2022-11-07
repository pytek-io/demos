from reflect_html import *
from reflect_antd import Rate


def app():
    return div([Rate(allowHalf=True, defaultValue=2.5)])
