from .common import *

figure = make_subplots(specs=[[{"secondary_y": True}]])

figure.add_trace(moving_average(input_1, 2, "blue"))
figure.add_trace(moving_average(input_1, 10, "yellow"))
figure.add_trace(candle_stick(input_1), secondary_y=False)
figure.update_yaxes(title_text="<b>Stock price</b> USD", secondary_y=False)


figure.add_trace(scatter(input_2, "red"), secondary_y=True)
figure.update_yaxes(title_text="<b>Rate</b> percent", secondary_y=True)

figure.update_layout(title_text=f"{input_1.name} vs {input_2.name[:30]}", title_x=0.5)

figure.add_annotation(
    x=datetime.date(2022, 7, 1), y=150, text="sth happened here!", showarrow=True, arrowhead=1
)
# figure.update_xaxes(title_text="xaxis title")

