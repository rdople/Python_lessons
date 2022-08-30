# Створи три функції, які обчислюють суму чисел у списку cycles_list
# #     з рекурсією
loop_list = list(input("Enter some sequence of numbers(recurs):"))


def recurs_loop_list(loop_list, el=0):
    result = 0
    if el >= len(loop_list):
        return 0
    return int(loop_list[el]) + recurs_loop_list(loop_list, el + 1)


print(f"{recurs_loop_list(loop_list)=}")

print(f"\nSECOND TASK")
# Створи функцію яка обчислює числа Фібоначчі.
# Функція приймає порядковий номер числа послідовності.
fib_user_input = int(input("Enter a number: "))

def fibonacci(serial_number):
    a, b = 1, 1
    for i in range(serial_number):
        print(a)
        a, b = b, a + b
    return None

fibonacci(fib_user_input)

#     Надрукуй 4 рядки: помідор -> м'ясо -> сир -> хліб, умови:
# #         Створи 4 функції, кожна друкує свій шар
# #         Викликай лише одну функцію
# #         Використай синтаксис декораторів
# #         Очікуваний результат друку:
# #             помідор
# #             м'ясо
# #             сир
# #             хліб
print(f"\nTHIRD TASK")
def my_product_list(add_product):
    def add_bread():
        print(f"хліб")

    def temp_list():
        print(f"помідор")
        add_product()
        print(f"сир")
        add_bread()
    return temp_list


@my_product_list
def add_meat():
    print(f"м'ясо")


add_meat()
