import socket
import sys

if len(sys.argv) != 2:
    print("Użycie: python3 zad5.py <hostname>")
    sys.exit(1)

hostname = sys.argv[1]

try:
    ip = socket.gethostbyname(hostname)
    print(f"Adres IP dla hosta: \'{hostname}\' to \'{ip}\'")
except socket.gaierror:
    print(f"Nie można znaleźć adresu IP dla hosta: \'{hostname}\'")
    sys.exit(1)

sys.exit(0)