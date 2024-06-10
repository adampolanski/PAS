import socket
import sys
import re

class Port:
    def __init__(self, number, open, service):
        self.number = number
        self.open = open
        self.service = service

    def __str__(self):
        return f"Port: {self.number}, Usługa: {self.service}"
    
    def __repr__(self):
        return f"Port: {self.number} [{'Otwarty' if self.open else 'Zamknięty'}], Usługa: {self.service}]"

debug = True

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
    service = None
    open = False
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    if debug: print (f"Próba połączenia z adresem: \'{ip}\' na porcie: \'{port}\'")
    if s.connect_ex((ip, port)) == 0:
        open = True
        print(f"Znaleziono otwarty port: \'{port}\'")
    try:
        service = socket.getservbyport(port)
    except OSError as e:
        service = None

    if open:
        open_ports.append(Port(port, open, service))
    
    s.close()

print(f"\nOtwarte porty na serwerze: \'{ip}\': {open_ports}")

sys.exit(0)