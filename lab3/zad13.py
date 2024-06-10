import socket
import sys

ip = "127.0.0.1"
port = 2910
data = "ed 74 0b 55 00 24 ef fd 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 6e 20 70 79 74 68 6f 6e 20 69 73 20 66 75 6e"
data = data.split(" ")

src_port = int(data[0], 16) * 256 + int(data[1], 16)
dst_port = int(data[2], 16) * 256 + int(data[3], 16)
length = int(data[4], 16) * 256 + int(data[5], 16)
checksum = int(data[6], 16) * 256 + int(data[7], 16)
data = "".join([chr(int(i, 16)) for i in data[8:]])

message = f"zad14odp;src;{src_port};dst;{dst_port};data;{data}"

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(message.encode(), (ip, port))
    s.settimeout(5)
    data, address = s.recvfrom(1024)
    print(f"Odpowiedź serwera: \'{ip}\' na porcie: \'{port}\' to: {data.decode()}")
    s.close()
except ConnectionRefusedError:
    print(f"Nie udało się nawiązać połączenia z serwerem: \'{ip}\' na porcie: \'{port}\'")
    sys.exit(1)

sys.exit(0)
