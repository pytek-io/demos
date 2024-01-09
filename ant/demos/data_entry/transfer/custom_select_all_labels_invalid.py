from render_antd import Transfer
from render_html import *


def app():
    return Transfer(dataSource=mockData, targetKeys=targetKeys, onChange=setTargetKeys, render=item => item.title, selectAllLabels=selectAllLabels)
def app():
    return App()