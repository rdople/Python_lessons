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
url_to_get = 'https://jsonplaceholder.typicode.com/posts/1'
url_to_post = 'https://jsonplaceholder.typicode.com/posts/'
file_path = "./API_data/response.json"
image_path = "./API_data/image.jpg"
picture_to_save = "https://images.squarespace-cdn.com/content/v1/51acece5e4b0a54238b8c10c/" \
                  "1620928649582-QPB2E507Y3SJBSD5LNO3/Valraven_Angle_Back_Red_2.JPG?format=2500w"


try:
    response = requests.request(url=url_to_post, method="GET")
    response_to_object = json.loads(response.content)
    with open(file_path, "w") as fh:
        json.dump(response_to_object, fh, indent=4)
        print(f"{response_to_object=}")
except:
    print(f"Error, please check request: {response.status_code=}")

# Прочитай інформацію з файлу та зроби HTTP запит на збереження
with open(file_path, "r+") as fh:
    data_to_upload = json.load(fh)
    print(f"{data_to_upload=}, {type(data_to_upload)=}")
    post_data = requests.post(url=url_to_post, data="data_to_upload")
    print(f"Successfully uploaded: {post_data.status_code=}")

#     Завантаж будь-яку картинку з інтернета, збережи її

response = requests.get(picture_to_save)
if response.status_code == 200:
    with open(image_path, 'wb') as fh:
        fh.write(response.content)