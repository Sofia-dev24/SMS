import requests

# https://webcom.mobi/ пример одного из сервисов

user = "InGeo"  # логин под которым регистрировались
password = "parol"  # пароль
sender = "Ingeo"  # подпись отправителя
receiver = "79222266728"  # номер отправителя
text = "Hello"

url = f"https://my3.webcom.mobi/sendsms.php?user={user}&pwd={password}&sadr={sender}&dadr={receiver}&text={text}"
try:
    response = requests.get(url)

    if response.status_code == 200:
        print("Сообщение успешно отправлено")
    else:
        print("Ошибка при отправке сообщения")
except Exception as e:
    print(f"Непредвиденная ошибка {e}")
