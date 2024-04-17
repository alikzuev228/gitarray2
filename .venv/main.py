from TK_1 import *
from TK_2 import *
from TK_3 import *
from TK_4 import *
import importlib

tk5_module = importlib.import_module("TK-5")

count = int(input("Введіть кількість значень: "))
my_list = input_values(count)
print("Введені значення:", my_list)

print("Мінімальне та максимальне значення:", min_max_values(my_list))
print("Список, кожний елемент якого поділений на середнє значення:", divide_by_mean(my_list))
print("Список, кожний елемент якого помножений на середнє значення:", multiply_by_mean(my_list))
print("Список, кожний елемент якого - це квадратний корінь від вхідного значення:", tk5_module.square_root(my_list))

