def input_values(count):
    values = []
    for i in range(count):
        value = int(input("Введіть значення {}: ".format(i+1)))
        values.append(value)
    return values
