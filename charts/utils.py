import io

import render_html as html


def matplotlib_to_svg(fig):
    content = io.StringIO()
    fig.savefig(content, format="svg")
    return html.inline_svg(content.getvalue())


def mplfnance_plot(df, **kwargs):
    """
    Display a mpl finance graph as a png. Left here for reference (better to
    return the plot as an svg and use the method above)
    """
    content = BytesIO()
    mpf.plot(df, savefig=content, **kwargs)
    return inline_png(base64.b64encode(content.getvalue()).decode("ascii"))
