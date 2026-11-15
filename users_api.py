import requests

def get_user(user_id):
    try:
        response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}', timeout=5)
    except requests.exceptions.Timeout:
        print("Сервер не ответил вовремя")
        return None
    except requests.exceptions.ConnectionError:
        print('Нет соединения с сервером')
        return None
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print('Пользователь не найден')
        return None
    else:
        print(f'Ошибка сервера: {response.status_code}')
        return None

if __name__ == '__main__':
    user = get_user(1)
    if user:
        print(user["name"])

    user = get_user(999)
    print(user)