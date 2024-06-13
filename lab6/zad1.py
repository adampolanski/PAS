# Do wykonania zadań możesz wykorzystać konta pocztowe:
# •pas2017@interia.pl z hasłem P4SInf2017
# •pasinf2017@interia.pl z hasłem P4SInf2017
# 1. Wykorzystując protokół telnet, oraz serwer ESMTP działający pod adresem interia.pl na porcie 587
# wyślij wiadomość e-mail używając komend protokołu ESMTP.

import socket
import sys
import ssl
import base64

def base64_to_text(text):
    try:
        return str(base64.b64decode(text))
    except:
        return str(base64.b64decode(text).decode('utf-8'))


def text_to_base64(text):
    try:
        print(f"Text: {text} -> {str(base64.b64encode(bytes(text)).decode())}")
        return str(base64.b64encode(bytes(text)).decode())
    except:
        print(f"Text: {text} -> {str(base64.b64encode(text.encode()).decode())}")
        return str(base64.b64encode(text.encode()).decode())

def read_command(s):
    data = s.recv(1024)
    data = data.decode('utf-8')
    print(f"Odpowiedź serwera: {data}")
    return data

def send_command(s, command):
    s.send((command + "\r\n").encode())
    data = s.recv(1024)
    data = data.decode('utf-8')
    print(f"Odpowiedź serwera: {data}")
    return data

def send_only_command(s, command):
    s.send((command + "\r\n").encode())

# gmail
ip = "smtp.gmail.com"
port = 587

sender_usr = "pas2017@interia.pl"
sender_pwd = "P4SInf2017"

receiver_usr = "adampolanski02@gmail.com"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((ip, port))
    print(f"Udało się nawiązać połączenie z serwerem: \'{ip}\' na porcie: \'{port}\'")

    s.settimeout(5)

    read_command(s)
    send_command(s, "EHLO PAS-ESMTP-TEST")
    send_command(s, "STARTTLS")

    context = ssl.create_default_context()
    s = context.wrap_socket(s, server_hostname=ip)

    send_command(s, "AUTH LOGIN")
    send_command(s, text_to_base64(sender_usr))
    result = send_command(s, text_to_base64(sender_pwd))
    if not result.startswith("235"):
        raise Exception("Błąd autoryzacji")

    send_command(s, f"MAIL FROM: <{sender_usr}>")
    send_command(s, f"RCPT TO: <{receiver_usr}>")
    send_command(s, "DATA")

    send_command(s, f"From: {sender_usr}")
    send_command(s, f"To: {receiver_usr}")
    send_command(s, "Subject: Testowy e-mail")
    send_command(s, "To jest testowy e-mail wysłany przez protokół ESMTP")
    send_command(s, ".")
    send_command(s, "QUIT")

except ConnectionRefusedError:
    print(f"Serwer o adresie: \'{ip}\' na porcie: \'{port}\' jest niedostępny")
    s.close()
    sys.exit(1)
except socket.timeout:
    print("Przekroczono limit czasu")
    s.close()
    sys.exit(1)
except Exception as e:
    print(e)
    s.close()
    sys.exit(1)

finally:
    s.close()

sys.exit(0)