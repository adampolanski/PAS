# serwer testowy dla zad1

import socket
import sys
import time

ip = "127.0.0.1"
port = 13

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(1)
    conn, addr = s.accept()
    print(f"Połączono z adresem: {addr}")
    conn.send(time.ctime().encode('utf-8'))
    conn.close()
    s.close()
except ConnectionRefusedError:
    print(f"Nie udało się nawiązać połączenia z serwerem: \'{ip}\' na porcie: \'{port}\'")
    sys.exit(1)

sys.exit(0)