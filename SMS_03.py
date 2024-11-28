import requests
import re
import json
from tkinter import *
from tkinter import messagebox as mb

from sms_main_02 import receiver


def check_balance(login, password):
    url = "https://my3.webcom.mobi/json/balance.php"
    headers = {"Content-type": "text/json; charset=utf-8"}

    data = {"login": login, "password": password}

    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            response_data = response.json()
            return response_data['money']
        else:
            mb.showerror("Ошибка!", f"Произошла ошибка {response.status_code}")
            return None
    except Exception as e:
        mb.showerror("Ошибка!", f"Произошла непредвиденная ошибка {e}.")


def validate_phone_number(phone_number):
    pattern = r"^79\d{9}$"
    return bool(re.match(pattern, phone_number))


def send_sms():
    user = "InGeo_Group"  # логин под которым регистрировались
    password = "parol"  # пароль
    sender = "InGeo_Group"  # подпись отправителя
    receiver = receiver_entry.get()
    text = text_entry.get()
    balance = check_balance(user, password)
    if balance:
        if float(balance) > 10:
            if not validate_phone_number(receiver):
                mb.showerror("Ошибка!", "Некорректный номер телефона")
            else:
                url = (f"https://my3.webcom.mobi/sendsms.php?user={user}&pwd={password}"
                       f"&sadr={sender}&dadr={receiver}&text={text}")
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        mb.showinfo("Отправление", "Сообщение успешно отправлено.")
                    else:
                        mb.showerror("Ошибка!", "Ошибка при отправке сообщения.")
                except Exception as e:
                    mb.showerror("Ошибка!", f"Непредвиденная ошибка {e}.")
        else:
            mb.showinfo("Отправление", "Недостаточно средств.")
    else:
        mb.showerror("Ошибка!", "Не удалось получить информацию о балансе.")


window = Tk()
window.title("Отправка СМС")
window.geometry("250x150")

Label(text="Номер получателя: ").pack()
receiver_entry = Entry()
receiver_entry.pack()

Label(text="Введите текст СМС").pack()
text_entry = Entry()
text_entry.pack()

send_button = Button(text="Отправить СМС", command=send_sms)
send_button.pack()


window.mainloop()
