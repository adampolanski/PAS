import socket
import sys
import re

if len(sys.argv) != 3:
    print("Użycie: python3 zad7.py <hostname> <port>")
    sys.exit(1)

hostname = sys.argv[1]
port = sys.argv[2]

if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", hostname):
    try:
        ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        print(f"Nie można znaleźć adresu IP dla hosta: \'{hostname}\'")
        sys.exit(1)
else:
    ip = hostname

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, int(port)))
    print(f"Udało się nawiązać połączenie z serwerem: \'{ip}\' na porcie: \'{port}\'")
    print(f"Usługa uruchomiona na porcie: \'{port}\': {socket.getservbyport(int(port))}")
    s.close()
except ConnectionRefusedError:
    print(f"Nie udało się nawiązać połączenia z serwerem: \'{ip}\' na porcie: \'{port}\'")
    sys.exit(1)
except OSError as e:
    print(f"Nie znaleziono usługi na porcie: \'{port}\'")

sys.exit(0)