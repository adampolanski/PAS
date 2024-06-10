#!/usr/bin/env python

# modyfikacje: 
# socket.sendto wymaga zakodowania danych (bez tej modyfikacji serwer nie działa poprawnie)
# dekodowanie danych przy odbieraniu danych od klienta

import socket, select, sys
from time import gmtime, strftime

HOST = '127.0.0.1'
PORT = 2906

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.bind((HOST, PORT))
except socket.error as msg:
    # print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    print(f'Bind failed. Error Code : {msg[0]} Message {msg[1]}')
    sys.exit()

# print "[%s] UDP ECHO Server is waiting for incoming connections on port %s ... " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), PORT)
print(f'[{strftime("%Y-%m-%d %H:%M:%S", gmtime())}] UDP ECHO Server is waiting for incoming connections on port {PORT} ... ')

try:
    while True:

        data, address = sock.recvfrom(4096)
        data = data.decode()

        # print '[%s] Received %s bytes from client %s. Data: %s' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), len(data), address, data)
        print(f'[{strftime("%Y-%m-%d %H:%M:%S", gmtime())}] Received {len(data)} bytes from client {address}. Data: {data}')

        if data:

            try :
                print(str(data))
                hostname = socket.gethostbyaddr(str(data))
                sent = sock.sendto(str(hostname[0]).encode(), address)
                # print '[%s] Sent %s bytes bytes back to client %s.' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), sent, address)
                print(f'[{strftime("%Y-%m-%d %H:%M:%S", gmtime())}] Sent {sent} bytes bytes back to client {address}.')

            # except socket.herror, e:
            except socket.herror as e:
                sent = sock.sendto("Sorry, an error occurred in gethostbyaddr".encode(), address)
                # print '[%s] Sent %s bytes bytes back to client %s.' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), sent, address)
                print(f'[{strftime("%Y-%m-%d %H:%M:%S", gmtime())}] Sent {sent} bytes bytes back to client {address}.')
finally:
    sock.close()
