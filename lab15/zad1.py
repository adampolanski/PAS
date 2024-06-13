# Napisz program klienta, który połączy sie z serwerem TCP działającym pod adresem 127.0.0.1 na
# określonym porcie TCP, a następnie będzie w pętli wysyłał do niego tekst wczytany od użytkownika, i
# odbierał odpowiedzi.

import socket
import sys

ip = "127.0.0.1"
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((ip, port))
    print(f"Udało się nawiązać połączenie z serwerem: \'{ip}\' na porcie: \'{port}\'")

    while True:
        message = input("Podaj wiadomość do wysłania: ")
        s.send(message.encode())

        data = s.recv(1024).decode('utf-8')
        print(f"Odpowiedź serwera: {data}")
        if data == 'exit':
            break

except Exception as e:
    print(f"Nie udało się nawiązać połączenia z serwerem: \'{ip}\' na porcie: \'{port}\'")
    print(e)

finally:
    s.close()
    print("Zamknięto połączenie z serwerem.")

sys.exit(0)