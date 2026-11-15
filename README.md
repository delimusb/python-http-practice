# Упражнение по HTTP-запросам на Python

Практика работы с REST API через библиотеку `requests` на учебном сервере
[JSONPlaceholder](https://jsonplaceholder.typicode.com).

- `users_api.py` — получение пользователя по id
- `posts_api.py` — создание, изменение и удаление постов

## Запуск
```
git clone https://github.com/delimusb/python-http-practice.git
cd python-http-practice
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python users_api.py
```

## Что я изучил
- Запросы и ответы HTTP, коды статуса (2xx, 4xx, 5xx)
- Методы GET, POST, PATCH, DELETE и их связь с CRUD
- Отправка JSON в теле запроса
- Обработка сетевых ошибок и таймаутов
- Вынос повторяющегося кода в общую функцию (принцип DRY)