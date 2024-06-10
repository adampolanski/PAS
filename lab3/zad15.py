import socket
import sys

ip = "127.0.0.1"
port = 2911

data = "45 00 00 4e f7 fa 40 00 38 06 9d 33 d4 b6 18 1b c0 a8 00 02 0b 54 b9 a6 fb f9 3c 57 c1 0a 06 c1 80 18 00 e3 ce 9c 00 00 01 01 08 0a 03 a6 eb 01 00 0b f8 e5 6e 65 74 77 6f 72 6b 20 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 73 20 66 75 6e"
data = data.split(" ")

# 4 bity
version = int(data[0][0], 16)
# 4 bity
ihl = int(data[0][1], 16)
# 8 bitów
ds_ecn = int(data[1], 16)
# 16 bitów
total_length = int(data[2], 16) * 256 + int(data[3], 16)
# 16 bitów
identification = int(data[4], 16) * 256 + int(data[5], 16)
# 16 bitów
flag_fragment = int(data[6], 16) * 256 + int(data[7], 16)
# 8 bitów
ttl = int(data[8], 16)
# 8 bitów
protocol = int(data[9], 16)
# 16 bitów
header_checksum = int(data[10], 16) * 256 + int(data[11], 16)
# 32 bitów
src_ip = ".".join([str(int(i, 16)) for i in data[12:16]])
# 32 bitów
dst_ip = ".".join([str(int(i, 16)) for i in data[16:20]])
# 16 bitów
src_port = int(data[20], 16) * 256 + int(data[21], 16)
# 16 bitów
dst_port = int(data[22], 16) * 256 + int(data[23], 16)
# 32 bity
sequence_number = int(data[24], 16) * 256 ** 3 + int(data[25], 16) * 256 ** 2 + int(data[26], 16) * 256 + int(data[27], 16)
# 32 bity
acknowledgement_number = int(data[28], 16) * 256 ** 3 + int(data[29], 16) * 256 ** 2 + int(data[30], 16) * 256 + int(data[31], 16)
# 4 bity
header_length = int(data[32][0], 16)
# 4 bity
reserved = int(data[32][1], 16)
# 8 bitów
flags = int(data[33], 16)
# 16 bitów
window_size = int(data[34], 16) * 256 + int(data[35], 16)
# 16 bitów
checksum = int(data[36], 16) * 256 + int(data[37], 16)
# 16 bitów
urgent_pointer = int(data[38], 16) * 256 + int(data[39], 16)
# 12 * 8 bitów
options = "".join([chr(int(i, 16)) for i in data[40:52]])

data = "".join([chr(int(i, 16)) for i in data[52:]])

message_a = f"zad15odpA;ver;{version};srcip;{src_ip};dstip;{dst_ip};type;{protocol}"
message_b = f"zad15odpB;srcport;{src_port};dstport;{dst_port};data;{data}"

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(message_a.encode(), (ip, port))
    s.settimeout(5)
    data, address = s.recvfrom(1024)
    print(f"Odpowiedź serwera: \'{ip}\' na porcie: \'{port}\' to: {data.decode()}")
    s.sendto(message_b.encode(), (ip, port))
    s.settimeout(5)
    data, address = s.recvfrom(1024)
    print(f"Odpowiedź serwera: \'{ip}\' na porcie: \'{port}\' to: {data.decode()}")
    s.close()
except ConnectionRefusedError:
    print(f"Nie udało się nawiązać połączenia z serwerem: \'{ip}\' na porcie: \'{port}\'")
    sys.exit(1)

sys.exit(0)
