from render_antd import Button, Table
from render_html import *

loading, selectedRowKeys = this.loading, this.selectedRowKeys
def app(_):
    return div([div([Button("Reload", type="primary", onClick=this.start, disabled=!hasSelected, loading=loading), span(""{hasSelected ? `Selected $"{selectedRowKeys.length}" items` : ''}"", style=dict(marginLeft=8))], style=dict(marginBottom=16)), Table(rowSelection=rowSelection, columns=columns, dataSource=data)])
def app(_):
    return App()