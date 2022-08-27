from traceback import print_exc
from reflect_html import *
from reflect_antd import Radio, Badge
from reflect import autorun, create_observable



def app():
    # note we need to define the state outside the method rendering the components otherwise it wouldn't be persisted between updates.
    counters = [create_observable(value) for value in [1, 2]]

    def update_counters(value):
        counters[value] += 1
        # FIXME: this crashes the application
        # raise Exception("kaboom")

    result = Radio.Group(
        [
            Badge(Radio.Button("Click Me", value=0), count=lambda: counters[0]),
            Badge(Radio.Button("Not Me", value=1), count=lambda: counters[1]),
        ],
        buttonStyle="solid",
        onChange=update_counters,
    )
    autorun(lambda: print(result()))
    return result
