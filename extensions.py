import redis
import requests
import time

def handle_redis_connection_error():
    try:
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        return r
    except redis.ConnectionError:
        print("Ошибка подключения к Redis")
        return None

def handle_image_caching_error(image_url):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Не удалось получить изображение: {image_url}")
            return None
    except requests.RequestException as e:
        print(f"Ошибка при запросе изображения: {e}")
        return None

def handle_user_data_error(user_data, user_id):
    try:
        if user_id not in user_data:
            print(f"Данные для пользователя {user_id} не найдены.")
            return None
        return user_data[user_id]
    except Exception as e:
        print(f"Ошибка обработки данных пользователя {user_id}: {e}")
        return None

def handle_general_error(error_message):
    """Общая функция для обработки неожиданных ошибок."""
    print(f"Произошла ошибка: {error_message}")