from render_html import *
from render_antd import Tree, Input
Search = Input.Search
key = node.key
value = e.value
searchValue, expandedKeys, autoExpandParent = this.searchValue, this.expandedKeys, this.autoExpandParent
getParentKey = span([""{beforeStr}"", span(""{searchValue}"", className="site-tree-search-value"), ""{afterStr}""])
getParentKey = span(""{item.title}"")
def app():
    return div([Search(style=dict(marginBottom=8), placeholder="Search", onChange=this.onChange), Tree(onExpand=this.onExpand, expandedKeys=expandedKeys, autoExpandParent=autoExpandParent, treeData=loop(gData))])
def app():
    return SearchTree()