# Створи функцію, яка приймає параметри start та end,
# підсумовує всі цілі числа від значення start до величини end включно.
# Якщо користувач задасть перше число більше, ніж друге, поміняй їх місцями

while True:
    try:
        number_1 = int(input("Enter first number:"))

    except ValueError as error:
        print("Enter only digits")
    try:
        number_2 = int(input("Enter second number:"))
        break
    except ValueError as error:
        print("Enter only digits")


def int_sum(start, end):
    if start > end:
        start, end = end, start
    return sum([el for el in range(start, end + 1)])


print(int_sum(number_1, number_2))


# Створи функцію, яка відображає число секунд у вигляді дні:години:хвилини:секунди.
# Функція може прийняти число як рядок так і як ціле число.


def time_representation(sec):
    days = sec // (24 * 3600)
    sec = sec % (24 * 3600)
    hours = sec // 3600
    sec %= 3600
    minutes = sec // 60
    sec %= 60
    print(f"дні:години:хвилини:секунди")
    return print(days, hours, minutes, sec, sep=':')


while True:
    try:
        user_input_seconds = int(input("Enter total seconds: "))
        break
    except ValueError as error:
        print("Enter only digits")

time_representation(user_input_seconds)

# Створи три функції, які обчислюють суму чисел у списку cycles_list
# #     з for-циклом
loop_list = list(input("Enter some sequence of numbers:"))


def for_loop_list(loop_list):
    # loop_list = list(input("Enter some sequence of numbers(for):"))
    print(f"{loop_list=}", type(loop_list))
    sum_for = 0
    for x in loop_list:
        sum_for += int(x)
    print(f"{sum_for=}")
    return None


#     з while-циклом


def while_loop_list(loop_list):
    # loop_list = list(input("Enter some sequence of numbers(while):"))
    print(f"{loop_list=}", type(loop_list))
    counter = 0
    sum_while = 0
    while counter < len(loop_list):
        sum_while += int(loop_list[counter])
        counter += 1

    print(f"{sum_while=}")
    return None


for_loop_list(loop_list)
while_loop_list(loop_list)
