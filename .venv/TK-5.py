import math


def square_root(lst):
    if not lst:
        return []

    squared_root_list = [math.sqrt(x) for x in lst]

    return squared_root_list