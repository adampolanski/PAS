# Napisz program klienta, który nawiąże połączenie (handshake) z serwerem obsługującym protokół WebSocket, działającym pod adresem ws://echo.websocket.org na porcie 80.

import socket
import sys

ip = "echo.websocket.org"
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((ip, port))
    print(f"Udało się nawiązać połączenie z serwerem: \'{ip}\' na porcie: \'{port}\'")

    s.settimeout(5)

    request = "GET /chat HTTP/1.1\r\n"
    request += "Host: echo.websocket.org\r\n"
    request += "Upgrade: websocket\r\n"
    request += "Connection: Upgrade\r\n"
    request += "Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n"
    request += "Origin: http://websocket.org\r\n"
    request += "Sec-WebSocket-Protocol: chat\r\n"
    request += "Sec-WebSocket-Version: 13\r\n"
    request += "\r\n"

    s.send(request.encode())

    data = s.recv(1024 * 1024 * 10)
    data = data.decode('utf-8')
    print(f"Odpowiedź serwera: {data}")

except Exception as e:
    print(f"Nie udało się nawiązać połączenia z serwerem: \'{ip}\' na porcie: \'{port}\'")
    print(e)

finally:
    s.close()
    print("Zamknięto połączenie z serwerem.")

sys.exit(0)