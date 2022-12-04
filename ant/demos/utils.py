
def find_index(iterable, predicate, start=0):
    for index, value in enumerate(iterable):
        if index >= start and predicate(value):
            return index