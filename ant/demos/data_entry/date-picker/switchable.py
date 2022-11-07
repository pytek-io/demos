import reflect as r
import reflect_antd as antd
import reflect_html as html

Option = antd.Select.Option


def picker_with_type(picker_type, onChange):
    if picker_type == "time":
        return antd.TimePicker(onChange=onChange)
    if picker_type == "date":
        return antd.DatePicker(onChange=onChange)
    return antd.DatePicker(picker=picker_type, onChange=onChange)


def app():
    picker_type = antd.Select(
        [
            Option("Time", value="time"),
            Option("Date", value="date"),
            Option("Week", value="week"),
            Option("Month", value="month"),
            Option("Quarter", value="quarter"),
            Option("Year", value="year"),
        ],
        defaultValue="time",
    )
    r.autorun(lambda: print(picker_type()))
    return antd.Space(
        [picker_type, picker_with_type(picker_type=picker_type, onChange=print)],
        direction="vertical",
    )
