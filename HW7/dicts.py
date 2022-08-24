#    Створи файл dicts.py у своєму проекті, виконуй завдання в ньому, використовуй англійську
#    Після виконання практичної роботи - запуш її у GitHub
# 1.Відтвори ASCII таблицю у вигляді словника, обов'язкові умови:
# ---Використай генератор словника
# ---Використай вбудовану функцію chr()
# 2. Реалізувати послідовність операцій яка:
#    -- Приймає від користувача пароль у вигляді цілого числа
#    -- Створює словник шифра метода одноалфавітної підстановки на базі пароля.
#    -- Тобто пароль - число на яке треба збільшити порядковий номер літери у алфавіті.
#    -- Шифрує строку на базі словника шифра. Приклад
#       -- Звичайний порядок "a" - 1, "b" - 2, ..., "z" - 26 -> словник "a"="a", "b"="b", ..., "z"="z"
#       -- З паролем у 4 порядок стає "a" - 5, "b" - 6, ..., "z" - 4 -> словник "a"="e", "b"="f", ..., "z"="d"
#       -- Рядок "hello" перетворюється на "lipps"
#    -- Друкує зашифровану строку
#    -- Приймає від користувача строку

# ** 1.Print ASCII table with keys and values, using dictionary generator:")
print(f"** 1.Print ASCII table with keys and values, using dictionary generator:")
generated_dict = {chr(element): element for element in range(127)}
print(f"{generated_dict=}\n")

# ** 2.SECOND_TASK
encrypted_user_input = ""
print(f"** 2.Print an encrypted string")
non_encrypted_user_input = input("Please enter your string which you want to encrypt:")
while True:
    try:
        pass_key = int(input("Enter your integer key:"))
        break
    except ValueError as error:
        print("Enter only digits")

for element in non_encrypted_user_input:
    encrypted_user_input += chr(ord(element) + pass_key)

print(f"{non_encrypted_user_input=}")
print(f"{encrypted_user_input=}")


