import os

import seaborn as sns

from demos.charts.utils import matplotlib_to_svg

sns.set_theme(style="ticks")


def app(_):
    os.environ["SEABORN_DATA"] = os.path.split(__file__)[0]
    penguins = sns.load_dataset("penguins")
    fig = sns.jointplot(
        data=penguins, x="bill_length_mm", y="bill_depth_mm", hue="species", kind="kde"
    )
    return matplotlib_to_svg(fig)
