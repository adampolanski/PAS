import socket
import sys

ip = "127.0.0.1"
port = 2901

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b"Hello world!", (ip, port))
data, addr = s.recvfrom(1024)

print(f"Odpowiedź serwera: \'{ip}\' na porcie: \'{port}\' to: {data.decode('utf-8')}")
sys.exit(0)