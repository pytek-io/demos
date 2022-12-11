import reflect as r
import reflect_antd as antd

optionLists = [
    {"value": "zhejiang", "label": "Zhejiang", "isLeaf": False},
    {"value": "jiangsu", "label": "Jiangsu", "isLeaf": False},
]


def app():
    options = r.create_observable(optionLists, key="optionLists")

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
                {"label": f"{target_option['label']} Dynamic 1", "value": "dynamic1"},
                {"label": f"{target_option['label']} Dynamic 2", "value": "dynamic2"},
            ]
            options.touch()

        r.schedule_callback(1.0, update)

    cascader = antd.Cascader(
        options=options, changeOnSelect=True, loadData=r.Callback(load_data)
    )
    r.autorun(lambda: print("changed", cascader()))
    return cascader
