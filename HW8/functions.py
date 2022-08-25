# Створи функцію, яка приймає параметри start та end,
# підсумовує всі цілі числа від значення start до величини end включно.
# Якщо користувач задасть перше число більше, ніж друге, поміняй їх місцями

# while True:
#     try:
#         number_1 = int(input("Enter first number:"))
#
#     except ValueError as error:
#         print("Enter only digits")
#     try:
#         number_2 = int(input("Enter second number:"))
#         break
#     except ValueError as error:
#         print("Enter only digits")
#
#
# def int_sum(start, end):
#     if start > end:
#         start, end = end, start
#     return sum([el for el in range(start, end + 1)])
#
#
# print(int_sum(number_1, number_2))

# Створи функцію, яка відображає число секунд у вигляді дні:години:хвилини:секунди.
# Функція може прийняти число як рядок так і як ціле число.


# def time_representation(sec):
#     days = sec // (24 * 3600)
#     sec = sec % (24 * 3600)
#     hours = sec // 3600
#     sec %= 3600
#     minutes = sec // 60
#     sec %= 60
#     print(f"дні:години:хвилини:секунди")
#     print(days, hours, minutes, sec, sep=':')
#     return None
#
#
# while True:
#     try:
#         user_input_seconds = int(input("Enter total seconds: "))
#         break
#     except ValueError as error:
#         print("Enter only digits")
#
# time_representation(user_input_seconds)


# Створи три функції, які обчислюють суму чисел у списку
#     з for-циклом





# Створи три функції, які обчислюють суму чисел у списку
#     з while-циклом
