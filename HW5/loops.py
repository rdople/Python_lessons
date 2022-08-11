#    Створи файл loops.py у своєму проекті, виконуй завдання в ньому, використовуй англійську
#     Після виконання практичної роботи - запуш її у GitHub
# Створи послідовність інструкцій у вигляді циклу, яка:
# Приймає від користувача рядок будь-яких символів, наприклад S f-FaGA a
# Друкує усі літери з рядку, які у верхньому регістрі, у прикладі вище це SFGA
# Друкує індекси усіх пробілів, якщо вони є, у прикладі вище це 1, 8
# Друкує усі гласні букви з рядка, у прикладі вище це aAa
# Якщо у рядку буде послідовність з трьох цифр, наприклад ab-c474f g - цикл переривається
# та друкується повідомлення про цю подію. Інакше друкується повідомлення про
# коректне завершення циклу
# Цикл один, працює один раз, відповіді виводяться у рядок, тобто у консолі буде
# роздруковано 3 рядки
# На базі калькулятора з практичного завдання у розділі Розгалуження,
# створи нескінченний цикл до доки користувач не введе exit замість будь-якого з
# операндів або оператора
vowels = 'aAeEiIoOuU'
is_vowel = ""
is_space = " "
up_symbols = ""
space_index = ""
is_digit = ""
user_input = input("Hello, please type your sentence here: ")
for index, value in enumerate(user_input):
    if value.isupper():
        up_symbols += value

    if value == is_space:
        space_index += str(index) + ","

    if value in vowels:
        is_vowel += value

    if value.isdigit():
        is_digit += value
    else:
        is_digit = ""
    if len(is_digit) == 3:
        print("Sequence of numbers is present")
        break
else:
    is_digit = ""
    print("You don't have any sequence of numbers")
#print(is_digit)
print(f"Uppercase symbols: {up_symbols} \n"
      f"Space indexes if it's True: {space_index[:-1]} \n"
      f"Vowels in input: {is_vowel} \n")





