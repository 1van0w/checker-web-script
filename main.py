import requests
import sys
import time
import webbrowser
from urllib.parse import urlparse
from subprocess import call


# Получение информации от пользователя
url = ""
domain = ""
args = sys.argv
if len(args) == 1:
    url = input('Введите URl сайта: ')
else:
    url = args[1]
domain = urlparse(url).netloc
speech = "Похоже что сейчас этот сайт в сети."

# Проверка значений и обработка ошибок
while True:
    try:
        res = requests.get(url)
        if res.status_code == requests.codes.ok:
            print("200\n" + domain + " сейчас в сети.")
            webbrowser.open(url,new=2)
            for i in range(2):
                call(["Уведомляем",domain,"сейчас в сети."])
                time.sleep(3)
            break
        time.sleep(10)
    except requests.ConnectionError as e:
        print("Проверьте свое подключение к интернету!")
        sys.exit(1)
    else:
        print("Произошла ошибка.")
        sys.exit(1)