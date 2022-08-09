counter = ""
vowels = 'aAeEiIoOuU'
is_vowel = ""
is_space = " "
up_symbols = ""
space_index = ""
is_digit = 0
user_input = "S f-FaGA a4586"
for index, value in enumerate(user_input):
    if value.isupper():
        counter += value
        # print(letter)
        up_symbols += value

    if value == is_space:
        space_index += str(index) + ","

    if value in vowels:
        is_vowel += value

    if value.isdigit():
        # is_digit += is_digit + index
        print(f"{index=}, {value}")

print(f"Uppercase symbols: {up_symbols} \n"
      f"Space indexes if it's True: {space_index[:-1]} \n"
      f"Vowels in input: {is_vowel} \n")




