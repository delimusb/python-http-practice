import requests

BASE_URL = 'https://jsonplaceholder.typicode.com'

def send_request(method, path, data=None):
    try:
        return requests.request(method, BASE_URL + path, json=data, timeout=5)
    except requests.exceptions.Timeout:
        print("Сервер не ответил вовремя")
    except requests.exceptions.ConnectionError:
        print('Нет соединения с сервером')
    return None

def create_post(title, body):
    response = send_request('POST', '/posts', {'title' : title, 'body' : body})
    if response is None:
        return None
    if response.status_code == 201:
        return response.json()
    elif response.status_code == 404:
        print('Пост не найден')
    else:
        print(f'Ошибка: {response.status_code}')
    return None

def update_title(post_id, new_title):
    response = send_request('PATCH', f'/posts/{post_id}', {'title' : new_title})
    if response is None:
        return None
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print('Пост не найден')
    else:
        print(f'Ошибка: {response.status_code}')
    return None

def delete_post(post_id):
    response = send_request('DELETE', f'/posts/{post_id}')
    if response is None:
        return False
    if response.status_code == 200:
        return True
    elif response.status_code == 404:
        print('Пост не найден')
    else:
        print(f'Ошибка: {response.status_code}')
    return False

if __name__ == '__main__':
    post = create_post("Привет", "Это мой пост")
    print(post)

    post = update_title(1, "Изменённый заголовок")
    if post:
        print(post["title"])

    print(delete_post(1))

