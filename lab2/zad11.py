# Przy próbie wysłania wiadomości o długości większej niż 20 znaków, klient otrzymuje przyciętą wiadomość.

import socket
import sys

ip = "127.0.0.1"
port = 2908
message = input("Podaj wiadomość: ")

if len(message) < 20:
    message = message + " " * (20 - len(message))
elif len(message) > 20:
    message = message[:20]

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.send(message.encode())
    s.settimeout(5)
    data = s.recv(1024)
    print(f"Odpowiedź serwera: \'{ip}\' na porcie: \'{port}\' to: {data.decode()}")
    s.close()
except ConnectionRefusedError:
    print(f"Nie udało się nawiązać połączenia z serwerem: \'{ip}\' na porcie: \'{port}\'")
    sys.exit(1)

sys.exit(0)