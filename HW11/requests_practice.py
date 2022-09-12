#    Створи файл requests_practice.py у своєму проекті, виконуй завдання в ньому, використовуй англійську
##     Після виконання практичної роботи - запуш її у GitHub
##         Зроби HTTP запит на зчитування, збережи результат у файл
##         Прочитай інформацію з файлу та зроби HTTP запит на збереження
##         Вигадай ще кілька задач, попрактикуйся з модулем
##     Завантаж будь-яку картинку з інтернета, збережи її
##     Обирай будь-які завдання на PyCheckio та розв'язуй їх, у тебе достатньо знань та інструментів для цього)
import requests
import json

url_to_get = 'https://jsonplaceholder.typicode.com/posts/1'
url_to_post = 'https://jsonplaceholder.typicode.com/posts/'
file_path = "./API_data/response.json"
picture_path = "./API_data/image.jpg"
picture_to_save = "https://images.squarespace-cdn.com/content/v1/51acece5e4b0a54238b8c10c/" \
                  "1620928649582-QPB2E507Y3SJBSD5LNO3/Valraven_Angle_Back_Red_2.JPG?format=2500w"


# Зроби HTTP запит на зчитування, збережи результат у файл


def request_to_file(your_url, your_file):
    try:
        response = requests.request(url=your_url, method="GET")
        response_to_object = json.loads(response.content)
        with open(your_file, "w") as fh:
            json.dump(response_to_object, fh, indent=4)
            print(f"{response_to_object=}")
    except:
        print(f"Error, please check request: {response.status_code=}")
    return print(f"{response.status_code=}")


request_to_file(url_to_get, file_path)


# Прочитай інформацію з файлу та зроби HTTP запит на збереження


def file_to_post(your_file, your_url):
    with open(your_file, "r+") as fh:
        data_to_upload = json.load(fh)
        print(f"{data_to_upload=}, {type(data_to_upload)=}")
        post_data = requests.post(url=your_url, data="data_to_upload")
        return print(f"Successfully uploaded: {post_data.status_code=}")


file_to_post(file_path, url_to_post)


#     Завантаж будь-яку картинку з інтернета, збережи її

def save_image_from_web(picture, pic_path):
    response = requests.get(picture)
    if response.status_code == 200:
        with open(pic_path, 'wb') as fh:
            fh.write(response.content)
    return print(f"Picture downloading code: {response.status_code=}")


save_image_from_web(picture_to_save, picture_path)
