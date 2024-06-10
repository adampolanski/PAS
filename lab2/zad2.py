import socket
import sys

ip = "127.0.0.1"
port = 2900
message = input("Podaj wiadomość: ")

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.send(message.encode('utf-8'))
    data = s.recv(1024)
    s.close()
except ConnectionRefusedError:
    print(f"Nie udało się nawiązać połączenia z serwerem: \'{ip}\' na porcie: \'{port}\'")
    sys.exit(1)

print(f"Odpowiedź serwera: \'{ip}\' na porcie: \'{port}\' to: {data.decode('utf-8')}")
sys.exit(0)
