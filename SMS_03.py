import requests
import re
import json


def check_balance(login, password):
    url = "https://my3.webcom.mobi/json/balance.php"
    headers = {"Content-type: text/json; charset=utf-8;"}

    data = {"login": login, "password": password}

    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            response_data = response.json()
            print(response_data)
            print(f"Баланс: {response_data['money']} руб.")
        else:
            print(f"Произошла ошибка {response.status_code}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка {e}.")


def validate_phone_number(phone_number):
    pattern = r"^79\d{9}$"
    return bool(re.match(pattern, phone_number))


user = "InGeo_Group"  # логин под которым регистрировались
password = "parol"  # пароль
sender = "InGeo_Group"  # подпись отправителя
receiver = "79222266728"  # номер отправителя
text = "Hello"

balance = check_balance(user, password)
if balance:
    if balance > 10:
        if not validate_phone_number(receiver):
            print("Ошибка. Некорректный номер телефона")
        else:
            url = f"https://my3.webcom.mobi/sendsms.php?user={user}&pwd={password}&sadr={sender}&dadr={receiver}&text={text}"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print("Сообщение успешно отправлено")
                else:
                    print("Ошибка при отправке сообщения")
            except Exception as e:
                print(f"Непредвиденная ошибка {e}")
    else:
        print("Недостаточно средств.")
else:
    print("Не удалось получить информацию о балансе.")