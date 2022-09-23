# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x_coordinate = int(input('Введите координату Х: '))
y_coordinate = int(input('Введите координату Y: '))

if x_coordinate > 0 and y_coordinate > 0:
    print('Точка находится в I четверти плоскости')
if x_coordinate < 0 and y_coordinate > 0:
    print('Точка находится в II четверти плоскости')
if x_coordinate < 0 and y_coordinate < 0:
    print('Точка находится в III четверти плоскости')
if x_coordinate > 0 and y_coordinate < 0:
    print('Точка находится в IV четверти плоскости')
if x_coordinate == 0 and y_coordinate == 0:
    print('Точка находится в центре плоскости координат')    
if x_coordinate == 0:
    print('Точка находится на оси X')
if y_coordinate == 0:
    print('Точка находится на оси Y')
