import render_antd as antd


def app(_):
    return antd.Segmented(options=["Daily", "Weekly", "Monthly", "Quarterly", "Yearly"])
