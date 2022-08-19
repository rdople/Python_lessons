#Next task
incoming_list = [1, 2.1, "f", "2", 3, "1", 18, "df"]
# result_list = [value if type(value) == float else
#               # **2 if type(value) == int and value % 2 == 0
#                         else value = "-1"
#                for value in incoming_list
#                ]
# result_list = [value if type(value) == float else
#                :
#                    value **= 2 if (type(value) == int and value % 2 == 0) for value in incoming_list]
# *****
# list_b = [x if x < 0 else x**2 for x in list_a]
# Если x-отрицательное - берем x, в остальных случаях - берем квадрат x
# *****
    # value **= 2 if type(value) == int and value % 2 == 0 else
    # value type(value) == int and value % 2 != 0 else
    # value type(value) == str and value.isdigit() else
    # value = -1
# for value incoming_list]


res = [
    value if type(value) == float else
    value if type(value) == int and value % 2 == 0 else
    (value ** 2) if type(value) == int and value % 2 != 0 else
    (int(value) * 3) if type(value) == str and value.isdigit() else -1
    for value in incoming_list
]
print(res)






# [value
# if type(value) == float else
# value **= 2 if type(value) == int and value % 2 == 0
# else type(value) == int and value % 2 != 0
# else type(value) == str and value.isdigit()
# else value = -1
# for value incoming_list]
# [value if type(value) == float else -1 for el in mix_list]
# for value in incoming_list:
    # if type(value) == float:
    #     result_list.append(value)
    #
    # elif type(value) == int and value % 2 == 0:
    #     result_list.append(value)
    #
    # elif type(value) == int and value % 2 != 0:
    #     value **= 2
    #     result_list.append(value)
    #
    # elif type(value) == str and value.isdigit():
    #     value = int(value) * 3
    #     result_list.append(str(value))
    #
    # else:
    #     value = -1
    #     result_list.append(value)

# print(f"--Next task result--\n"
#       f"Information to check:\n"
#       f"Expected list by task: [1, 2.1, -1, '6', 9, '3', 18, -1]\n"
#       f"Formatted result list: {result_list}")
