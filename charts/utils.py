from reflect_html import inline_svg
from io import StringIO


def matplotlib_to_svg(fig):
    content = StringIO()
    fig.savefig(content, format="svg")
    return inline_svg(content.getvalue())


def mplfnance_plot(df, **kwargs):
    """
    Display a mpl finance graph as a png. Left here for reference (better to 
    return the plot as an svg and use the method above)
    """
    content = BytesIO()
    mpf.plot(df, savefig=content, **kwargs)
    return inline_png(base64.b64encode(content.getvalue()).decode("ascii"))
