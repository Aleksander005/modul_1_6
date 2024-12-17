from functools import update_wrapper

my_dict = {'Dima': 2000, 'Tima': 2001, 'Lena': 2002}
print(my_dict)
print(my_dict['Dima'])  # Выведите на экран одно значение по существующему ключ
print(my_dict.get('Petr'))  # дно по отсутствующему из словаря my_dict без ошибки.
my_dict.update({'Petr': 2003, 'Ilia': 2004})  # бавьте ещё две произвольные пары того же формата в словарь my_dict.
print(my_dict)
del my_dict['Ilia']  # Удалите одну из пар в словаре по существующему ключу из словаря my_dict
print(my_dict)
# множества
my_set = {1, 1, 'set', 'set', 1.1, 1.1}
print(my_set)
my_set.add(7.62)  # ('2') )) # добавляется только один элемент
print(my_set)
my_set.add((7.62, 8.88))  # добавление кортежа
print(my_set)
my_set.discard(1)  # удаление элемента
print(my_set)
