# Napisz program serwera, który działając pod adresem 127.0.0.1 oraz na określonym porcie TCP będzie
# losował liczbę i odbierał od klienta wiadomości. W przypadku, gdy w wiadomości klient przyśle do serwera
# coś innego, niż liczbę, serwer powinien poinformować klienta o błędzie. Po odebraniu liczby od klienta,
# serwer sprawdza, czy otrzymana liczba jest:
# •mniejsza od wylosowanej przez serwer
# •równa wylosowanej przez serwer
# •większa od wylosowanej przez serwer
# A następnie odsyła stosowną informację do klienta. W przypadku, gdy klient odgadnie liczbę, serwer
# powinien zakończyć działanie.

import socket
import sys
import random

ip = "127.0.0.1"
port = 2912

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((ip, port))

random_number = random.randint(0, 100)
print(f"Serwer wylosował liczbę: {random_number}")

while True:
    data, addr = s.recvfrom(1024)
    data = data.decode('utf-8')
    print(f"Odebrano wiadomość od klienta: {data}")
    if data == "exit":
        break

    try:
        number = int(data)
    except ValueError:
        s.sendto("Podana wartość nie jest liczbą".encode(), addr)
        continue

    if number < random_number:
        s.sendto("Liczba jest mniejsza".encode(), addr)
    elif number == random_number:
        s.sendto("Gratulacje, zgadłeś liczbę!".encode(), addr)
    else:
        s.sendto("Liczba jest większa".encode(), addr)
    
s.close()
sys.exit(0)