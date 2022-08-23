# Створи файл sets.py у своєму проекті, виконуй завдання в ньому, використовуй англійську
# Після виконання практичної роботи - запуш її у GitHub
# 1.Створити послідовність інструкцій, яка друкує результат аналізу 2 наборів
# текстових даних з будь-яких символів, отриманих від користувача
# --Список літер, які присутні в обох наборах, не зважаючи на регістр,Літери не повторювати
# --Список цифр, які є в першому або в другому наборі, але не в обох,Цифри не повторювати
# 2.Знайди та ознайомся з операторами |=, &=, -=, ^=, та методами які відповідають цим операторам.
# Наведи по 1 прикладу для кожного оператора, використовуй 3 множини одночасно у якості операндів
# 3.Розв'яжи онлайн завдання
# https://py.checkio.org/en/mission/shorter-set
#      FIRST TASK
first_user_input = set(input("Please, type something: "))
second_user_input = set(input("Type something again, it's not a joke): "))
common_letters = [el for el in first_user_input.intersection(second_user_input)
                  if el.isalpha()]
unique_numbers = [el for el in first_user_input.symmetric_difference(second_user_input)
                  if el.isdigit()]
print(f"{common_letters=}", type(common_letters))
print(f"{unique_numbers=}", type(unique_numbers))

#    SECOND TASK
print("\n#    SECOND TASK")
first_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
second_set = {1, 2, 3, 4, 5, 6}
third_set = {1, 2, 3, 4}


# ^= symmetric_difference_update
print(f"^= symmetric_difference_update")
third_set ^= second_set ^ first_set
print(f"{third_set=}\n")
#  third_set = 12347890


# -= difference_update
print(f"-= difference_update")
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_set = {2, 4, 6, 8}
numbers.difference_update(even_set)
print(f"{numbers=}")
print(f"{even_set=}\n")


# &= intersection_update

print(f"&= intersection_update")
none_result = numbers.intersection_update(second_set, third_set)
print(f"{none_result=}")
print(f"{numbers=}")
print(f"{second_set=}")
print(f"{third_set=}\n")


 # |= update
print(f"|= update")
numbers.update(second_set)
print(f"{numbers=}")









