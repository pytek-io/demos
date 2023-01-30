import reflect as r
import reflect_antd as antd

RangePicker = antd.DatePicker.RangePicker


def footer(content):
    return r.JSMethod("constant", f"""return '{content}'""", "arg")


def app():
    return antd.Space(
        [
            antd.DatePicker(renderExtraFooter=footer("Select date XYZ")),
            antd.DatePicker(renderExtraFooter=footer("Select time XYZ"), showTime=True),
            RangePicker(renderExtraFooter=footer("Select date range XYZ")),
            RangePicker(renderExtraFooter=footer("Select time XYZ"), showTime=True),
            antd.DatePicker(
                renderExtraFooter=footer("Select month XYZ"), picker="month"
            ),
        ],
        direction="vertical",
        size=12,
    )
