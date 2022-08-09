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
num_a = 0
num_b = 0
action = ""
result = None
quit_word = "exit"
while True:
    print("Now you're in calculator mode, enter two operands and basic actions")
    num_a = input("Enter your first number: ")
    if num_a == quit_word:
        break
    else:
        num_b = input("Enter your second number: ")
    if num_b == quit_word:
        break
    else:
        action = input(f"Enter operation symbol:"
                       f"\n P.S. Only * / + - ** operations expected: ")
        if action == quit_word:
            break
        else:
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
                    result = num_a / num_b if num_b != 0 else "Can't divide on zero!"
                case "**":
                    result = num_a ** num_b
                case _:
                    print("Bad symbol. Only * / + - ** operations expected")
            print(f"Your result: {result}")
            print("first", num_a, type(num_a))
            print("second", num_b, type(num_b))





