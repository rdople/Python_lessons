# Створи файл os_interaction.py у своєму проекті, виконуй завдання в ньому, використовуй англійську
# Після виконання практичної роботи - запуш її у GitHub
# Зайди на сторінку офіційної документації, ознайомся с функціоналом модуля
# Створи функцію яка збирає усю можливу інформацію про операційну систему та записує її у файл os_report.json

import os
import json
import getpass
import socket
from uuid import getnode as get_mac
import psutil

obj = {
    "user_name": getpass.getuser(),
    "ip": socket.gethostbyname(socket.getfqdn()),
    "mac": get_mac(),
    "cpu_freq": psutil.cpu_freq(),
    "os": os.environ["OS"],
    "computer_name": os.environ["COMPUTERNAME"],
    "system_drive": os.environ["SYSTEMDRIVE"],
    "system_root": os.environ["SYSTEMROOT"],
    "number_of_processors": os.environ["NUMBER_OF_PROCESSORS"], #or os.cpu_count( )
    "processor_identifier": os.environ["PROCESSOR_IDENTIFIER"],
    "processor_revision": os.environ["PROCESSOR_REVISION"]
}

with open("os_report.json", "w+") as fh:
    json.dump(obj, fh, sort_keys=True)
print(obj)
os.startfile("os_report.json") #відкриває записаний файл_
