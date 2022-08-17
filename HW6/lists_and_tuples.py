#    Створи файл lists_and_tuples.py у своєму проекті, виконуй завдання в ньому, використовуй англійську
#    Після виконання практичної роботи - запуш її у GitHub
#Створи послідовність інструкцій, яка отримує рядок від користувача та друкує кожне третє слово з цього рядка.
#Цикли не використовувати
# Створи генератор списка
#   Вхідний список [1, 2.1, "f", "2", 3, "1", 18, "df"]
#   Вихідний список [1, 2.1, -1, '6', 9, '3', 18, -1]
#   Як та які елементи потрапляють з вхідного до вихідного списка:
#   Елемент типу float
#   Елемент типу int та є парним
#   Елемент типу int та є непарним. Додатково звести у 2 ступінь. Приклад, елемент 3 -> 9
#   Елемент типу str у якому лише цифри. Додатково помножити на 3. Приклад, елемент "2" -> "6"
#   В інших випадках замість елемента підстав число -1


# First task
# you can use example text for checking
# Девки в озере купались, торт резиновый нашли. Целый день они питались, даже в школу не пошли.
# Expected result "['озере', 'резиновый', 'день', 'даже', 'не']"
user_input = input("Please enter some sentence:").split(" ")
print(f"Every third word: {user_input[2::3]}\n")

#Next task
incoming_list = [1, 2.1, "f", "2", 3, "1", 18, "df"]
res = [
    value if type(value) == float
    else value if type(value) == int and value % 2 == 0
    else (value ** 2) if type(value) == int and value % 2 != 0
    else str(int(value) * 3) if type(value) == str and value.isdigit()
    else -1
    for value in incoming_list
     ]
# result_list = []
# for value in incoming_list:
#     if type(value) == float:
#         result_list.append(value)
#
#     elif type(value) == int and value % 2 == 0:
#         result_list.append(value)
#
#     elif type(value) == int and value % 2 != 0:
#         value **= 2
#         result_list.append(value)
#
#     elif type(value) == str and value.isdigit():
#         value = int(value) * 3
#         result_list.append(str(value))
#
#     else:
#         value = -1
#         result_list.append(value)

print(f"--Next task result--\n"
      f"Information to check:\n"
      f"Expected list by task: [1, 2.1, -1, '6', 9, '3', 18, -1]\n"
      # f"Formatted result list:FOR::::: {result_list}\n"
      f"Formatted result list: {res}")











