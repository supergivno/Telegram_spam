from telethon import TelegramClient, events, sync
import os
from colorama import Fore, Back, Style

def cls():
    os.system('clear')

api_id = int(input(Fore.MAGENTA + " API ID: "))
api_hash = input(" API Hash: ")

client = TelegramClient('session_name', api_id, api_hash)

client.start()

cls()

print(Fore.CYAN + '''
  _____        _        _____
 |_   _|      | |      /  ___|
   | |    ___ | |  ___ \ `--.  _ __    __ _  _ __ ___
   | |   / _ \| | / _ \ `--. \| '_ \  / _` || '_ ` _ \
   | |  |  __/| ||  __//\__/ /| |_) || (_| || | | | | |
   \_/   \___||_| \___|\____/ | .__/  \__,_||_| |_| |_|
                              | |
                              |_|



''')

print(Fore.GREEN + """
 [1] Бесконечный спам | Infinity spam

 [2] Спам с указанным количеством сообщений | How many

""")


a = input(Fore.YELLOW + ' Выберите параметр | Choose parametr: ')

if a == "1":
    print(" ")
    print(Fore.BLUE + " ")
    idp = input("Введите id/nick пользователя Telegram: ")
    mes = input("Текст сообщения | Text of the message: ")
    print(Fore.RED + '   Атака успешно началась! ')
    while True:

        client.send_message(idp, mes)

elif a == "2":
    print(" ")
    print(" ")
    px = int(input(Fore.BLUE + " Введите количество сообщений: "))
    idp = input(" Введите id/nick пользователя Telegram: ")
    mes = input(" Текст сообщения | Text of the message: ")
    print(Fore.RED + '   Атака успешно началась! ')
    for i in range(px):
        client.send_message(idp, mes)

else:
    print(" Нету такого параметра | Wrong parametr")

