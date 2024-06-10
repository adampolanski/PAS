import socket
import sys

ip = "127.0.0.1"
port = 2902

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

a = input("Podaj pierwszą liczbę: ")
s.sendto(a.encode(), (ip, port))
op = input("Podaj operator: ")
s.sendto(op.encode(), (ip, port))
b = input("Podaj drugą liczbę: ")
s.sendto(b.encode(), (ip, port))
s.settimeout(5)
data, addr = s.recvfrom(1024)

print(f"Odpowiedź serwera: \'{ip}\' na porcie: \'{port}\' to: {data.decode('utf-8')}")
sys.exit(0)