# Створи файл flow_control
# Після виконання практичної роботи - запуш її у GitHub
# Створи послідовність інструкцій, яка реалізує функціонал калькулятора - складання, віднімання, поділ,
# множення, возведення в ступінь
#   Гарантована послідовність введення 3 параметрів: операнд 1, операнд 2, дія для калькулятора
#   Користувач може помилитися зі знаком арифметичної дії, у цьому разі вивести сповіщення
#   про некоректний знак
#   Гарантовано що операнди будуть типу int, float або комбінацією цих типів
#   Калькулятор мусить повернути результат типу int якщо якщо операнди були типу int
#   За бажанням - проаналізуй операнди та сповісти користувача про:
#  Тип операнду
#  Скільки порядків має операнд
#  Результат порівняння операндів

print("Now you're in calculator mode, enter two operands and basic actions")
num_a = input("Enter your first number: ")
num_b = input("Enter your second number: ")
result = None
action = input(f"Enter what operation you want to do with your two numbers"
               f"\n P.S. Only * / + - ** operations expected: ")
if action != "*" or "-" or "+" or "/" or "**":
    print(f"You've entered incorrect action symbol. \n"
          f"We can't calculate it. \n"
          f" Your result wil be None ")
#    action = input(f"You've entered incorrect action symbol. \n"
#                   f"Try again. Only * / + - ** operations expected: ")
num_a = float(num_a) if num_a.find(".") != -1 else int(num_a)
num_b = float(num_b) if num_b.find(".") != -1 else int(num_b)
match action:
    case "+":
        result = num_a + num_b
    case "-":
        result = num_a - num_b
    case "*":
        result = num_a * num_b
    case "/":
        result = num_a / num_b
    case "**":
        result = num_a ** num_b

print(f"Your result: {result}")
print("first", num_a, type(num_a))
print("second", num_b, type(num_b))


