
from reflect_html import inline_svg
from io import StringIO

def matplotlib_to_svg(fig):
    content = StringIO()
    fig.savefig(content, format="svg")
    return inline_svg(content.getvalue())
