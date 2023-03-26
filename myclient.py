import socket
import random
from threading import Thread
from datetime import datetime

# Задаем адрес и порт сервера для подключения
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000
separator_token = "<SEP>"  # Разделитель имени и соообщения

s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")

# Вводим ник пользователя
name = input("Enter your name: ")

#  Функция принимает  сообщения

def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print(message)


# запускаем слушатель в отдельном потоке
t = Thread(target=listen_for_messages)
# t.daemon = True
t.start()

while True:
    to_send = input()
    if to_send.lower() == 'q':
        break
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    to_send = f"[{date_now}] {name}{separator_token}{to_send}"
    s.send(to_send.encode())

s.close()
