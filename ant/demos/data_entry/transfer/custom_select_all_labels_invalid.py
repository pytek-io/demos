from render_html import *
from render_antd import Transfer
def app():
    return Transfer(dataSource=mockData, targetKeys=targetKeys, onChange=setTargetKeys, render=item => item.title, selectAllLabels=selectAllLabels)
def app():
    return App()