from reflect_html import *
from reflect_antd import Cascader
from reflect import autorun, make_observable
from reflect import schedule_callback, Callback


optionLists = [
    {
        "value": "zhejiang",
        "label": "Zhejiang",
        "isLeaf": False,
    },
    {
        "value": "jiangsu",
        "label": "Jiangsu",
        "isLeaf": False,
    },
]


def app():
    options = make_observable(optionLists, key="optionLists")

    def load_data(selected_options):
        target_label = selected_options[-1]["label"]
        target_option = next(
            option for option in options() if option["label"] == target_label
        )
        target_option["loading"] = True
        options.touch()

        def update():
            print("updated tree values")
            target_option["loading"] = False
            target_option["children"] = [
                {
                    "label": f"{target_option['label']} Dynamic 1",
                    "value": "dynamic1",
                },
                {
                    "label": f"{target_option['label']} Dynamic 2",
                    "value": "dynamic2",
                },
            ]
            options.touch()

        schedule_callback(1.0, update)

    cascader = Cascader(
        options=options,
        changeOnSelect=True,
        loadData=Callback(load_data),
    )
    autorun(lambda: print("changed", cascader()))
    return cascader
