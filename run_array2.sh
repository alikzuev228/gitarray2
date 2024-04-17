#!/bin/bash

python -m pip install numpy
python3 -m venv myenv


# Активуємо віртуальне середовище
source myenv/Scripts/activate

# Запускаємо програму array2
python3 .venv/main.py

# Деактивуємо віртуальне середовище
deactivate
