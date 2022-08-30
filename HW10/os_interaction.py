# Створи файл os_interaction.py у своєму проекті, виконуй завдання в ньому, використовуй англійську
# Після виконання практичної роботи - запуш її у GitHub
# Зайди на сторінку офіційної документації, ознайомся с функціоналом модуля
# Створи функцію яка збирає усю можливу інформацію про операційну систему та записує її у файл os_report.json

import os
import json

obj = {
    "os": os.environ["OS"],
    "computer_name": os.environ["COMPUTERNAME"],
    "user_name": os.environ["USERNAME"],
    "system_drive": os.environ["SYSTEMDRIVE"],
    "system_root": os.environ["SYSTEMROOT"],
    "number_of_processors": os.environ["NUMBER_OF_PROCESSORS"], #or os.cpu_count( )
    "processor_identifier": os.environ["PROCESSOR_IDENTIFIER"],
    "processor_revision": os.environ["PROCESSOR_REVISION"]
}

with open("os_report.json", "w") as fh:
    json.dump(obj, fh)
# print(os.environ)
# os.startfile("os_report.json") #відкриває записаний файл
