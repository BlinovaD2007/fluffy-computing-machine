# Задача 1
# volume_disket = 1.44 * 1024 * 1024
# page = 100
# line = 50
# symbol = 25
# inf_symbol = 4
# volume_book = page * line * symbol * inf_symbol
# num_book = volume_disket // volume_book
# print(num_book)

# Задача 2
# pi = 3.1415
# radius = 5
# side = 5
# perimetr = 4 * side
# area_circle = pi * radius**2
# circle = 2 * pi * radius
# print(round(area_circle,2))

# Задача 3
# s = 20*'0' + 50*'1' + 30*'2'
# str_numbers = s
# print(str_numbers)

# Задача 4
# speed = 4096
# time = 120
# coast = speed * time
# size = 500
# money = coast // size
# print(money)

# a = [1,2,-5,-25,73]
# b = len(a) # длина списка
# c = sum(a) # сумма
# a[4] = sum(a)//len(a)


# Задача 1
# numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# list = [2, -93, -2, 8, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# b = len(list)
# c = sum(list)
# numbers[4] = ()
# print(a)

# a = [1,2,-5,-25,73,105]
# b = [stat:step:stop]a
# print(a[ :3])
# print(a[3: ])

# mails = ["Письмо 1", "Письмо 2", "Письмо 3", "Письмо 4", "Письмо 5"]
# emails = mails [::-1]
# print(mails)

# results = [10, 8, 9, 7, 6, 9, 10, 8, 9, 10]
# sum(results)
# len(results)
# a = '10, 8, 9, 7, 6, 9, 10, 8, 9, 10'
# a.count('10, 8, 9, 7, 6, 9, 10, 8, 9, 10')
# min('10, 8, 9, 7, 6, 9, 10, 8, 9, 10')
# max('10, 8, 9, 7, 6, 9, 10, 8, 9, 10')

# list = '"яблоко", "банан", "опельсин", "виноград"'
# a = 'опельсин'
# a [0] = 'а'
# a = 'апельсин'

# Задача 9
group_124 = ['Даша', 'Соня', 'Фатима', 'Лиза', 'Алина', 'Эля', 'Рита',
              'Полина', 'Юра', 'Илья', 'Катя']
group_1 = group_124[:6]
# group_1 = group_124 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(group_1)
group_2 = group_124[6:]
# group_1 = group_124 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(group_2)