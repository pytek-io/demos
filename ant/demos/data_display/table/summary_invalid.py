from reflect_html import *
from reflect_antd import Table, Typography
Text = Typography.Text
def app():
    return[
 Table.Summary.Row([Table.Summary.Cell("Total"), Table.Summary.Cell(Text(""{totalBorrow}"", type="danger")), Table.Summary.Cell(Text(""{totalRepayment}""))]),
 Table.Summary.Row([Table.Summary.Cell("Balance"), Table.Summary.Cell(Text(""{totalBorrow - totalRepayment}"", type="danger"), colSpan=2)]),
]