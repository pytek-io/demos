import render_antd as antd


def app():
    return antd.Segmented(options=["Daily", "Weekly", "Monthly", "Quarterly", "Yearly"])
