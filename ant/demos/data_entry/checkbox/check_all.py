from reflect_html import *
from reflect_antd import Checkbox, Divider

from reflect import make_observable, autorun
from typing import List


PLAIN_OPTIONS = ["Apple", "Pear", "Orange"]
DEFAULT_CHECKED_LIST = ["Apple", "Orange"]


def app():
    checked_list = Checkbox.Group(options=PLAIN_OPTIONS, defaultValue=DEFAULT_CHECKED_LIST)
    indeterminate = lambda : bool(checked_list() and len(checked_list()) > 0)
    check_all = lambda : bool(checked_list() and len(checked_list()) > len(PLAIN_OPTIONS))
    autorun(lambda: print(checked_list()))
    autorun(lambda: print(indeterminate()))

    # def onChange(values: List[str]):
    #     indeterminate.set(values and len(values) < len(PLAIN_OPTIONS))
    #     check_all.set(len(values) == len(PLAIN_OPTIONS))

    def onCheckAllChange(value):
        checked_list.set(PLAIN_OPTIONS if value else [])
        indeterminate.set(False)
        check_all.set(value)

    return [
        Checkbox(
            "Check all",
            indeterminate=indeterminate,
            # onChange=onCheckAllChange,
            checked=check_all,
        ),
        Divider(),
        checked_list,
    ]
