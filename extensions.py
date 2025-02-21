import redis
import requests
import time

def handle_redis_connection_error():
    try:
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        return r
    except redis.ConnectionError:
        print("Redis connection error")
        return None

def handle_image_caching_error(image_url):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Failed to retrieve image: {image_url}")
            return None
    except requests.RequestException as e:
        print(f"Error requesting image: {e}")
        return None

def handle_user_data_error(user_data, user_id):
    try:
        if user_id not in user_data:
            print(f"User data for {user_id} not found.")
            return None
        return user_data[user_id]
    except Exception as e:
        print(f"Error processing user data for {user_id}: {e}")
        return None

def handle_general_error(error_message):
    """General function for handling unexpected errors."""
    print(f"An error occurred: {error_message}")
