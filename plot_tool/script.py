import datetime
from .common import moving_average, scatter, candle_stick
from plotly.subplots import make_subplots

figure = make_subplots(specs=[[{"secondary_y": True}]])
figure.add_trace(candle_stick(input_1), secondary_y=False)
figure.update_yaxes(title_text="<b>Stock price</b> USD", secondary_y=False)
figure.add_trace(moving_average(input_2, 2, "blue"))
figure.add_trace(moving_average(input_2, 10, "yellow"))
figure.add_trace(scatter(input_2, "red"), secondary_y=True)
figure.update_yaxes(title_text="<b>Rate</b> percent", secondary_y=True)
figure.update_layout(title_text=f"{input_1.name} vs {input_2.name}", title_x=0.5)
figure.add_annotation(
    x=datetime.date(2023, 8, 1),
    y=197,
    text="sth happened here!",
    showarrow=True,
    arrowhead=1,
)
