from render import Callback, create_observable
from render_antd import DatePicker, Space
from render_html import *

RangePicker = DatePicker.RangePicker


def controlled_date_picker():
    mode = create_observable("time")

    def onOpenChange(open_mode):
        if open_mode:
            mode.set("time")

    def test(*args):
        print(args)

    return DatePicker(
        # mode=mode,
        showTime=True,
        onOpenChange=Callback(onOpenChange),
        # onPanelChange=Callback(test),
    )


# def app(_):
#     return RangePicker(
#         placeholder=["Start month", "End month"],
#         format="YYYY-MM",
#         value=value,
#         mode=mode,
#         onChange=this.handleChange,
#         onPanelChange=this.handlePanelChange,
#     )


def app(_):
    raise NotImplementedError("Low level state management not supported")
    return Space([controlled_date_picker()], direction="vertical", size=12)
