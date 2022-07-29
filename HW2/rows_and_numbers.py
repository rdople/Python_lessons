# Створи файл rows_and_numbers.py у своєму проекті, виконуй завдання в ньому, використовуй англійську
# Після виконання практичної роботи - запуш її у GitHub
# Створи послідовність інструкцій, яка:
#     Отримує від користувача його ім'я, виводить на друк привітання для цього імені, використовуючи f-string
#     Отримує від користувача дрібне число, виводить на друк:
#         Отримане число
#         Ціле число (число без дрібної частини)
#         4ту ступінь цілого числа
#         Корінь цілого числа
#         Залишок від ділення цілого числа на 2

name_input = input("What's your name?  ")
welcome_text = f"Hello {name_input}! Nice too meet you! Your next step to enter some float numeric.\n"
num_input = input("Please, enter float num:  ")
print("Your num: ", num_input)
num_input = int(float(num_input))
print("Same num as Integer: ", num_input)
print("4th power of an Integer: ", num_input ** 4)
print("The square_root of an Integer: ", num_input ** 0.5)
print("The remainder from dividing an Integer by 2: ", num_input % 2)


