# Pod adresem 212.182.24.27 na porcie TCP o numerze 2912 działa serwer losujący liczby. Napisz program
# klienta, który będzie pobierał od użytkownika liczbę, a następnie będzie wysyłał ją do serwera w celu
# odgadnięcia wylosowanej przez serwer liczby. Po wysłaniu liczby klient powienien odbierać od serwera
# odpowiedź mówiącą o tym, czy udało nam się daną liczbę odgadnąć.

import socket
import sys

ip = "127.0.0.1"
port = 2912

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    s.connect((ip, port))
    print(f"Udało się nawiązać połączenie z serwerem: \'{ip}\' na porcie: \'{port}\'")

    s.settimeout(5)

    while True:
        number = input("Podaj liczbę: ")
        s.send(number.encode())
        if number == "exit":
            break
        data = s.recv(1024)
        data = data.decode('utf-8')
        print(f"Odpowiedź serwera: {data}")
except ConnectionRefusedError:
    print(f"Serwer o adresie: \'{ip}\' na porcie: \'{port}\' jest niedostępny")
    sys.exit(1)
finally:
    s.close()

sys.exit(0)
            