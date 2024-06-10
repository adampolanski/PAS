import socket
import sys
import re

if len(sys.argv) != 2:
    print("Użycie: python3 zad4.py <ip_address>")
    sys.exit(1)

ip = sys.argv[1]
if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
    print("Podany adres IP jest niepoprawny")
    sys.exit(1)

try:
    hostname = socket.gethostbyaddr(ip)
    print(f"Hostname dla adresu: \'{ip}\' to \'{hostname[0]}\'")
except socket.herror:
    print(f"Nie można znaleźć hosta dla adresu: \'{ip}\'")
    sys.exit(1)

sys.exit(0)