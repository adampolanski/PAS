import socket
import sys

hostname = "localhost"
port = 13

try:
    ip = socket.gethostbyname(hostname)
except socket.gaierror:
    print(f"Nie można znaleźć adresu IP dla hosta: \'{hostname}\'")
    sys.exit(1)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    data = s.recv(1024)
    s.close()
except ConnectionRefusedError:
    print(f"Nie udało się nawiązać połączenia z serwerem: \'{ip}\' na porcie: \'{port}\'")
    sys.exit(1)

print(f"Data i czas pobrane z serwera: \'{ip}\' na porcie: \'{port}\' to: {data.decode('utf-8')}")
sys.exit(0)