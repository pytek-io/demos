import render as r
import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html

RangePicker = antd.DatePicker.RangePicker


def app(_):
    smileIcon = ant_icons.SmileOutlined()
    picker1 = antd.DatePicker(suffixIcon=smileIcon)
    picker2 = antd.DatePicker(suffixIcon=smileIcon, picker="month")
    picker3 = RangePicker(suffixIcon=smileIcon)
    picker4 = antd.DatePicker(suffixIcon=smileIcon, picker="week")
    picker5 = antd.DatePicker(suffixIcon="ab")
    picker6 = antd.DatePicker(suffixIcon="ab", picker="month")
    picker7 = antd.DatePicker(suffixIcon="ab")
    picker8 = antd.DatePicker(suffixIcon="ab", picker="week")
    r.autorun(lambda: print("date picker1", picker1()))
    r.autorun(lambda: print("date picker2", picker2()))
    r.autorun(lambda: print("date picker3", picker3()))
    r.autorun(lambda: print("date picker4", picker4()))
    r.autorun(lambda: print("date picker5", picker5()))
    r.autorun(lambda: print("date picker6", picker6()))
    r.autorun(lambda: print("date picker7", picker7()))
    r.autorun(lambda: print("date picker8", picker8()))
    return antd.Space(
        [picker1, picker2, picker3, picker4, picker5, picker6, picker7, picker8],
        direction="vertical",
        size=12,
    )
