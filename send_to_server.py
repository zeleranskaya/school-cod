import requests


username = input('твое имя: ')

while True:
    text = input('введи текст сообщения: ')

# переносит запрос в get_from_server
# запаковываем в словарь
    requests.get(
          'http://127.0.0.1:5000/send_messages',
          json={'username': username, 'text': text}
     )