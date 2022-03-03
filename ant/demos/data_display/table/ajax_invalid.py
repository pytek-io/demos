from reflect_html import *
from reflect_antd import Table
pagination = this.pagination
data, pagination, loading = this.data, this.pagination, this.loading
def app():
    return Table(columns=columns, rowKey=record => record.login.uuid, dataSource=data, pagination=pagination, loading=loading, onChange=this.handleTableChange)
def app():
    return App()