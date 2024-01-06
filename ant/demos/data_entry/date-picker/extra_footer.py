import render as r
import render_antd as antd

RangePicker = antd.DatePicker.RangePicker


def footer(content):
    return r.js_arrow(f"constant_{content}", f"() => '{content}'")


def app():
    return antd.Space(
        [
            antd.DatePicker(renderExtraFooter=footer("Select date XYZ")),
            antd.DatePicker(renderExtraFooter=footer("Select time XYZ"), showTime=True),
            RangePicker(renderExtraFooter=footer("Select date range XYZ")),
            RangePicker(renderExtraFooter=footer("Select time range XYZ"), showTime=True),
            antd.DatePicker(
                renderExtraFooter=footer("Select month XYZ"), picker="month"
            ),
        ],
        direction="vertical",
        size=12,
    )
