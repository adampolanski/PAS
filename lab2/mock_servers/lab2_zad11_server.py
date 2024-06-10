#!/usr/bin/env python

import socket
import sys
from time import gmtime, strftime

HOST = '127.0.0.1'
PORT = 2908
MAX_PACKET_LENGTH = 20

def recvall(sock, msgLen):
    msg = ""
    bytesRcvd = 0

    while bytesRcvd < msgLen:

        chunk = sock.recv(msgLen - bytesRcvd)

        if not chunk:
            break

        bytesRcvd += len(chunk)
        msg += str(chunk)

    return msg

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    # print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

s.listen(1000)

# print "[%s] TCP ECHO (fixed-length messages) Server is waiting for incoming connections ... " % strftime("%Y-%m-%d %H:%M:%S", gmtime())
print(f"[{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] TCP ECHO (fixed-length messages) Server is waiting for incoming connections ... ")

while True:

    connection, client_address = s.accept()

    try:
        # print "[%s] Client %s connected ... " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), client_address)
        print(f"[{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] Client {client_address} connected ... ")

        while True:
            try :
                data = recvall(connection, MAX_PACKET_LENGTH)
                # print "[%s] Client %s sent \'%s\' " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), client_address, data)
                print(f"[{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] Client {client_address} sent \'{data}\' ")

                if data:

                        # print "[%s] Sending back to client %s ... " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), data)
                        print(f"[{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] Sending back to client {data} ... ")
                        connection.sendall(data.encode())
                else:
                    # print "[%s] Client %s disconnected ... " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), client_address)
                    print(f"[{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] Client {client_address} disconnected ... ")
                    break
            # except socket.error, e:
            except socket.error as e:
                    # print "[%s] Something happened, but I do not want to bother you ... %s " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), e)
                    print(f"[{strftime('%Y-%m-%d %H:%M:%S', gmtime())}] Something happened, but I do not want to bother you ... {e} ")
                    exit(1)

    finally:
        connection.close()
