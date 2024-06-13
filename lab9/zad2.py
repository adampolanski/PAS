# Pod adresem httpbin.org na porcie TCP o numerze 80 działa serwer obsługujący protokół HTTP w
# wersji 1.1. Pod odnośnikiem /image/png udostępnia obrazek. Napisz program klienta, który połączy się
# z serwerem, a następnie pobierze obrazek i zapisze go na dysku. Jakich nagłówków HTTP należy użyć?

import socket
import sys

ip = "httpbin.org"
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((ip, port))
    print(f"Udało się nawiązać połączenie z serwerem: \'{ip}\' na porcie: \'{port}\'")

    s.settimeout(5)

    request = "GET /image/png HTTP/1.1\r\n"
    request += "Host: httpbin.org\r\n"
    request += "User-Agent: Safari/537.36\r\n"
    request += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n"
    request += "Accept-Language: pl-PL,pl;q=0.8,en-US;q=0.5,en;q=0.3\r\n"
    request += "Accept-Encoding: gzip, deflate\r\n"
    request += "Connection: keep-alive\r\n"
    request += "\r\n"

    s.send(request.encode())

    data = s.recv(1024 * 1024 * 100)

    data = data.split(b"\r\n\r\n")[1]

    with open("image.png", "wb") as file:
        file.write(data)

except Exception as e:
    print(f"Nie udało się nawiązać połączenia z serwerem: \'{ip}\' na porcie: \'{port}\'")
    print(e)
finally:
    s.close()
    print("Zamknięto połączenie z serwerem.")

sys.exit(0)