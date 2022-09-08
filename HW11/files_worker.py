#    Створи папку schedules та файл files_worker.py у своєму проекті, виконуй завдання в ньому,
#    використовуй англійську
#     Після виконання практичної роботи - запуш її у GitHub

# Створи schedules/schedule.csv будь-яким доступним тобі способом
#     Імена стовпчиків:
#        departure point; departure time; destination point; arrival time; cost ticket
#     Внеси кілька рядків відповідних даних
import csv
import json


file_path_csv = "./schedules/schedule.csv"
file_path_json = "./schedules/schedule.json"


def csv_filler():
    with open(file_path_csv, mode='w', newline='', encoding='utf-8') as fh:
        fieldnames = ['departure point', 'departure time', 'destination point', 'arrival time', 'cost ticket']
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()

        writer.writerow({'departure point': 'Kyiv', 'departure time': '09:44:00', 'destination point': 'Rome FCO',
                         'arrival time': '17:25:00', 'cost ticket': 17433})
        writer.writerow({'departure point': 'Kharkiv', 'departure time': '09:56:00', 'destination point': 'Warsaw WMI',
                         'arrival time': '17:25:00', 'cost ticket': 13345})
        writer.writerow({'departure point': 'Mariupol', 'departure time': '10:00:00', 'destination point': 'Warsaw WMI',
                         'arrival time': '17:25:00', 'cost ticket': 120975})
        writer.writerow({'departure point': 'Odesa', 'departure time': '09:36:00', 'destination point': 'Munich MUC',
                         'arrival time': '17:30:00', 'cost ticket': 50478})
        writer.writerow({'departure point': 'Lviv', 'departure time': '09:46:00', 'destination point': 'Kaunas KUN',
                         'arrival time': '17:40:00', 'cost ticket': 22789})
        writer.writerow({'departure point': 'Donetsk', 'departure time': '09:51:00', 'destination point': 'Barcelona BCN',
                         'arrival time': '17:15:00', 'cost ticket': 123456})
        writer.writerow({'departure point': 'Dnipro', 'departure time': '10:26:00', 'destination point': 'Ibiza IBZ',
                         'arrival time': '17:53:00', 'cost ticket': 5000})
        writer.writerow({'departure point': 'Sumy', 'departure time': '10:01:00', 'destination point': 'Santiago SCL',
                         'arrival time': '17:51:00', 'cost ticket': 25006})

    return None


csv_filler()


#Створи функцію яка читає вміст schedule.csv та повертає весь контент файлу у вигляді словника або списка
def csv_to_dict(filename):
    converted_list = []
    with open(filename) as file_obj:
        reader = csv.DictReader(file_obj)
        for row in reader:
            converted_list.append(dict(row))
    print(converted_list)
    return converted_list

convert_dict = csv_to_dict(file_path_csv)

#Створи функцію яка записує отриманий контент до файлу schedules/schedule.json
    # Ключі у записаному файлі мають буди відсортовані
    # Вкладеності всередині файлу мають бути оформлені відступами у 4 пробіли


def csv_result_to_json(object_to_file):
    with open(file_path_json, "w") as fh:
        json.dump(object_to_file, fh, indent=4, sort_keys=True)


csv_result_to_json(convert_dict)