from render_html import *
from render_antd import Table, Button
loading, selectedRowKeys = this.loading, this.selectedRowKeys
def app():
    return div([div([Button("Reload", type="primary", onClick=this.start, disabled=!hasSelected, loading=loading), span(""{hasSelected ? `Selected $"{selectedRowKeys.length}" items` : ''}"", style=dict(marginLeft=8))], style=dict(marginBottom=16)), Table(rowSelection=rowSelection, columns=columns, dataSource=data)])
def app():
    return App()