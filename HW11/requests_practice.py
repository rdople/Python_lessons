#    Створи файл requests_practice.py у своєму проекті, виконуй завдання в ньому, використовуй англійську
##     Після виконання практичної роботи - запуш її у GitHub
##         Зроби HTTP запит на зчитування, збережи результат у файл
##         Прочитай інформацію з файлу та зроби HTTP запит на збереження
##         Вигадай ще кілька задач, попрактикуйся з модулем
##     Завантаж будь-яку картинку з інтернета, збережи її
##     Обирай будь-які завдання на PyCheckio та розв'язуй їх, у тебе достатньо знань та інструментів для цього)
import requests
import json
# Зроби HTTP запит на зчитування, збережи результат у файл
file_path = "./API_data/response.json"
image_path = "./API_data/image.jpg"
try:
    response = requests.request(url='https://jsonplaceholder.typicode.com/posts/1', method="GET")
    response_to_object = json.loads(response.content)
    with open(file_path, "w") as fh:
        json.dump(response_to_object, fh, indent=4)
except:
    print(f"{response.status_code=}")

# Прочитай інформацію з файлу та зроби HTTP запит на збереження
with open(file_path, "r+") as fh:
    data_to_upload = json.load(fh)
    print(f"{data_to_upload=}, {type(data_to_upload)=}")
    post_data = requests.post(url='https://jsonplaceholder.typicode.com/posts/', data="data_to_upload")
    print(post_data.status_code)

#     Завантаж будь-яку картинку з інтернета, збережи її
picture_to_save = "http://craphound.com/images/1006884_2adf8fc7.jpg"
response = requests.get(picture_to_save)
if response.status_code == 200:
    with open(image_path, 'wb') as f:
        f.write(response.content)