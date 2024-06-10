# przetestowano na google.com / otwarte porty(1 - 1024): 80, 443

import socket
import sys
import re

debug = False

if len(sys.argv) != 2:
    print("Użycie: python3 zad7.py <hostname>")
    sys.exit(1)

hostname = sys.argv[1]

if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", hostname):
    try:
        ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        print(f"Nie można znaleźć adresu IP dla hosta: \'{hostname}\'")
        sys.exit(1)
else:
    ip = hostname

open_ports = []

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    if debug: print (f"Próba połączenia z adresem: \'{ip}\' na porcie: \'{port}\'")
    if s.connect_ex((ip, port)) == 0:
        open_ports.append(port)
        print(f"Udało się nawiązać połączenie z serwerem: \'{ip}\' na porcie: \'{port}\'")
    s.close()

print(f"\nOtwarte porty na serwerze: \'{ip}\': {open_ports}")

sys.exit(0)