import reflect as r
import reflect_antd as antd
import reflect_html as html

RangePicker = antd.DatePicker.RangePicker


def app():
    footer = lambda content: r.js("constant", content)
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
