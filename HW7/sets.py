# Створи файл sets.py у своєму проекті, виконуй завдання в ньому, використовуй англійську
# Після виконання практичної роботи - запуш її у GitHub
# 1.Створити послідовність інструкцій, яка друкує результат аналізу 2 наборів
# текстових даних з будь-яких символів, отриманих від користувача
# --Список літер, які присутні в обох наборах, не зважаючи на регістр
# --Список цифр, які є в першому або в другому наборі, але не в обох
# 2.Знайди та ознайомся з методами групи update для множин, та операторами які їм відповідають.
# За умови використання 3 множин одночасно, наведи по 1 прикладу для кожної update дії.
# Залиш коментарі для ясності
# 3.Розв'яжи онлайн завдання
# https://py.checkio.org/en/mission/shorter-set

first_user_input = set(input("Please, type something: "))
second_user_input = set(input("Type something again, it's not a joke): "))
common_letters = [el for el in first_user_input.intersection(second_user_input)
                  if el.isalpha()]
unique_numbers = [el for el in first_user_input.symmetric_difference(second_user_input)
                  if el.isdigit()]
print(f"{common_letters=}", type(common_letters))
print(f"{unique_numbers=}", type(unique_numbers))

















