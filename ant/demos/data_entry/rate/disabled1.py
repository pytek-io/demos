from reflect_html import *
from reflect_antd import Rate

def app():
    return div([Rate(disabled=True, defaultValue=2)])