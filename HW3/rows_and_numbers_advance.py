# Створи файл rows_and_numbers_advance.py у своєму проекті, виконуй завдання в ньому, використовуй англійську
# Після виконання практичної роботи - запуш її у GitHub
# Створи послідовність інструкцій, яка:
# 1. Отримує від користувача ім'я, де кожна літера може буте як маленького так і великого регістру,
# також можливі пробіли перед та після імені, наприклад wiLLiAm
# 2. Очищує ім'я від знаків пробілу спочатку та вкінці (знайти метод для рядків, який це робить)
# 3. Друкує привітання для цього імені у форматі перша літера велика, інші маленькі
# 4. Друкує кількість літер у імені
# 5. Друкує ім'я задом наперед

user_input = input("Hi, type your name:")
print(f"User name in origin: {user_input}")
user_input = user_input.strip()
print(f"User name without whitespaces:{user_input} ")
user_input = user_input.capitalize()
print(f"Hello my dear friend {user_input} !")
print(f"Amazing! Your name {user_input} consists of {len(user_input)} letters!")
print(f"Also, I can help you to spell your own name backwards, like this: {user_input[::-1]}")




















