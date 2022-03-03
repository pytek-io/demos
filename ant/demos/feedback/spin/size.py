from reflect_html import *
from reflect_antd import Spin, Space


def app():
    return Space([Spin(size="small"), Spin(), Spin(size="large")], size="middle")
