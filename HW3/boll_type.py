# Створи файл boll_type.py у своєму проекті, виконуй завдання в ньому, використовуй англійську
# Після виконання практичної роботи - запуш її у GitHub
# Виправ помилку у порівнянні 3 ! 5
# Наведи усі комбінації порівнянь для 5 _ 5, при яких результат буде True
# Наведи 5 комбінацій з логічних операторів (or, and, not) та дужок, так щоб результат у виразі True _ True _ False був True
# Порівняй логічні значення None та 7
# Порівняй логічні значення пустої строки та виразу 10 - 1


#1 Виправ помилку у порівнянні 3 ! 5
compare_1: bool = (3 != 5)
print(f"{compare_1=}")

#2 Наведи усі комбінації порівнянь для 5 _ 5, при яких результат буде True
print("#2.1 task", 5 == 5)
print("#2.2 task", 5 is 5)

#3 Наведи 5 комбінацій з логічних операторів
# (or, and, not) та дужок, так щоб результат у виразі True _ True _ False був True
is_true_1 = True and True or False
print(f"{is_true_1=}")
is_true_2 = (True and True) and not False
print(f"{is_true_2=}")
is_true_3 = True and (True or False)
print(f"{is_true_3=}")
is_true_4 = True or (True and False)
print(f"{is_true_4=}")
is_true_5 = (True or True) or False
print(f"{is_true_5=}")

#4 Порівняй логічні значення None та 7
is_none_1 = 7 is None
print(f"{is_none_1=}")
is_none_2 = 7 is not None
print(f"{is_none_2=}")

#5 Порівняй логічні значення пустої строки та виразу 10 - 1
empty_str = ""
exp = bool(10-1)
print("Compare empty string 1:", empty_str or exp)
print("Compare empty string 2:", empty_str is exp)
print("Compare empty string 3:", empty_str == exp)
print("Compare empty string 4:", empty_str != exp)

