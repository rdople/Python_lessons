# Створи три функції, які обчислюють суму чисел у списку cycles_list
# #     з рекурсією
# loop_list = list(input("Enter some sequence of numbers(recurs):"))
#
#
# def recurs_loop_list(loop_list, el=0):
#     result = 0
#     if el >= len(loop_list):
#         return 0
#     return int(loop_list[el]) + recurs_loop_list(loop_list, el + 1)
#
#
# print(f"{recurs_loop_list(loop_list)=}")

# fibonacci
# fib_user_input = int(input("Enter a number: "))
#
# def fibonacci(serial_number):
#     a, b = 1, 1
#     for i in range(serial_number):
#         print(a)
#         a, b = b, a + b
#     return None
#
# fibonacci(fib_user_input)

# Надрукуй 4 рядки: помідор -> м'ясо -> сир -> хліб, умови:
    # Створи 4 функції, кожна друкує свій шар
    # Викликай лише одну функцію
    # Використай синтаксис декораторів