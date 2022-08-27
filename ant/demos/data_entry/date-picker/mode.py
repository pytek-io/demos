from reflect_html import *
from reflect_antd import DatePicker, Space
from reflect import create_observable
from reflect import Callback

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


# def app():
#     return RangePicker(
#         placeholder=["Start month", "End month"],
#         format="YYYY-MM",
#         value=value,
#         mode=mode,
#         onChange=this.handleChange,
#         onPanelChange=this.handlePanelChange,
#     )


def app():
    raise NotImplementedError("Low level state management not supported")
    return Space([controlled_date_picker()], direction="vertical", size=12)
