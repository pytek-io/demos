import reflect as r
import reflect_antd as antd
import reflect_html as html

RangePicker = antd.DatePicker.RangePicker


def app():
    def onOk(value):
        print("onOk: ", value)

    def onChange(values):
        print("Selected Time: ", values)
        print(
            "Formatted Selected Time: ",
            [value.strftime("%Y-%M-%D %H:%m") for value in values],
        )

    date_picker = antd.DatePicker(showTime=True, onOk=r.Callback(onOk))
    range_picker = RangePicker(
        showTime=dict(format="HH:mm"),
        format="YYYY-MM-DD HH:mm",
        onChange=onChange,
        onOk=r.Callback(onOk),
    )
    r.autorun(lambda: print("date picker", date_picker()))
    r.autorun(lambda: print("range picker", range_picker()))
    return antd.Space([date_picker, range_picker], direction="vertical", size=12)
