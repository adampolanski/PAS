import socket
import sys

ip = "127.0.0.1"
port = 2907

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

hostname = str(input("Podaj nazwę hosta: "))
s.sendto(hostname.encode(), (ip, port))
s.settimeout(5)
data, addr = s.recvfrom(1024)

print(f"Odpowiedź serwera: \'{ip}\' na porcie: \'{port}\' to: {data.decode()}")
sys.exit(0)