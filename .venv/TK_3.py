def divide_by_mean(lst):
    if not lst:
        return []

    mean_value = sum(lst) / len(lst)
    divided_list = [value / mean_value for value in lst]

    return divided_list