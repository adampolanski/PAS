import socket
import sys

ip = "127.0.0.1"
port = 2909
data = "0b 54 89 8b 1f 9a 18 ec bb b1 64 f2 80 18 00 e3 67 71 00 00 01 01 08 0a 02 c1 a4 ee 00 1a 4c ee 68 65 6c 6c 6f 20 3a 29"
data = data.split(" ")

# 16 bitów
src_port = int(data[0], 16) * 256 + int(data[1], 16)
# 16 bitów
dst_port = int(data[2], 16) * 256 + int(data[3], 16)
# 32 bitów   
sequence_number = int(data[4], 16) * 256 ** 3 + int(data[5], 16) * 256 ** 2 + int(data[6], 16) * 256 + int(data[7], 16)
# 32 bitów
acknowledgement_number = int(data[8], 16) * 256 ** 3 + int(data[9], 16) * 256 ** 2 + int(data[10], 16) * 256 + int(data[11], 16)
# 16 bitów
hdr_res_flags = int(data[12], 16) * 256 + int(data[13], 16)
# 16 bitów
window = int(data[14], 16) * 256 + int(data[15], 16)
# 16 bitów
checksum = int(data[16], 16) * 256 + int(data[17], 16)
# 16 bitów
urgent_pointer = int(data[18], 16) * 256 + int(data[19], 16)
# 12 * 8 bitów
options = "".join([chr(int(i, 16)) for i in data[20:32]])

data = "".join(chr(int(i, 16)) for i in data[32:])

message = f"zad13odp;src;{src_port};dst;{dst_port};data;{data}"

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
