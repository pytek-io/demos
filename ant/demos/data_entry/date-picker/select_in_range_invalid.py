from render import Callback, autorun, create_observable, js
from render_antd import DatePicker
from render_html import *

RangePicker = DatePicker.RangePicker


def app():
    raise NotImplementedError("low level effect not supported")
    value = create_observable()
    dates = create_observable([])
    hackValue = create_observable()

    def result():
        #   const disabledDate = current => {
        #     if (!dates || dates.length === 0) {
        #       return false;
        #     }
        #     const tooLate = dates[0] && current.diff(dates[0], 'days') > 7;
        #     const tooEarly = dates[1] && dates[1].diff(current, 'days') > 7;
        #     return tooEarly || tooLate;
        #   };

        def onOpenChange(is_open):
            if is_open:
                hackValue.set([])
                dates.set([])
            else:
                hackValue.set(None)

        autorun(lambda: print("dates", dates()))
        autorun(lambda: print("hackValue", hackValue()))
        autorun(lambda: print("value", value()))
        return RangePicker(
            value=value,
            disabledDate=js("selectRangeDisabledDate", dates()),
            onCalendarChange=Callback(dates.set),
            onOpenChange=Callback(onOpenChange),
        )

    return result