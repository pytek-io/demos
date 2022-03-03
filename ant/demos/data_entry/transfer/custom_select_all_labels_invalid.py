from reflect_html import *
from reflect_antd import Transfer
def app():
    return Transfer(dataSource=mockData, targetKeys=targetKeys, onChange=setTargetKeys, render=item => item.title, selectAllLabels=selectAllLabels)
def app():
    return App()