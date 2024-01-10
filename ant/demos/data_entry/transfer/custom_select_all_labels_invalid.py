from render_antd import Transfer
from render_html import *


def app(_):
    return Transfer(dataSource=mockData, targetKeys=targetKeys, onChange=setTargetKeys, render=item => item.title, selectAllLabels=selectAllLabels)
def app(_):
    return App()