def multiply_by_mean(lst):
    if not lst:
        return []

    mean_value = sum(lst) / len(lst)
    multiplied_list = [value * mean_value for value in lst]

    return multiplied_list