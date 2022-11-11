import os

import seaborn as sns
from demos.charts.utils import matplotlib_to_svg

sns.set_theme(style="ticks")

def app():
    # setting parent folder as cache location
    os.environ["SEABORN_DATA"] = os.path.split(__file__)[0]
    # Load the penguins dataset
    penguins = sns.load_dataset("penguins")
    # Show the joint distribution using kernel density estimation
    fig = sns.jointplot(
        data=penguins,
        x="bill_length_mm",
        y="bill_depth_mm",
        hue="species",
        kind="kde",
    )
    return matplotlib_to_svg(fig)
