# Домашняя работа по уроку "Стиль кода часть II. Цикл While."

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = 0
print('Список', my_list, 'положительные числа из списка')

while count < len(my_list):
    number = my_list[count]    
    count = count + 1
    if number == 0:
        continue
    elif number < 0:
        print('Встретилось отрицательное число:', number)
        break
    elif count == len(my_list):
        print(number)
        print('Список закончился')
    else:
        print(number)