# Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).

quarter_Number = int(input('Введите номер четверти: '))

if quarter_Number == 1:
    print('Х (0; + бесконечности), Y(0; + бесконечности)')
if quarter_Number == 2:
    print('Х (0; - бесконечности), Y(0; + бесконечности)')
if quarter_Number == 3:
    print('Х (0; - бесконечности), Y(0; - бесконечности)')
if quarter_Number == 4:
    print('Х (0; + бесконечности), Y(0; - бесконечности)')
if quarter_Number < 1 or quarter_Number > 4:
    print('Error! Такой плоскости нет')
