from render_antd import Select
from render_html import *

selectedItems = this.selectedItems
def app(_):
    return Select([""{filteredOptions.map(item => (", Select.Option(""{item}"", key=item, value=item), "))}""], mode="multiple", placeholder="Inserted are removed", value=selectedItems, onChange=this.handleChange, style=dict(width='100%'))
def app(_):
    return SelectWithHiddenSelectedOptions()