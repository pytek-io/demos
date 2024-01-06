from render_html import *
from render_antd import Select
selectedItems = this.selectedItems
def app():
    return Select([""{filteredOptions.map(item => (", Select.Option(""{item}"", key=item, value=item), "))}""], mode="multiple", placeholder="Inserted are removed", value=selectedItems, onChange=this.handleChange, style=dict(width='100%'))
def app():
    return SelectWithHiddenSelectedOptions()