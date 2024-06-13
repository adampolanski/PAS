import select, socket, Queue
if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    inputs = [server_socket]
    outputs = []
    message_queues = {}
    while inputs:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)
        for s in readable:
            if s is server_socket:
                connection, client_address = s.accept()
                connection.setblocking(0)
                inputs.append(connection)
                message_queues[connection] = Queue.Queue()
            else:
                data = s.recv(1024)
                if data:
                    if data == b'shutdown':
                        s.sendall(b'shutdown')
                        break
                    message_queues[s].put(data)
                    if s not in outputs:
                        outputs.append(s)
                else:
                    if s in outputs:
                        outputs.remove(s)
                    inputs.remove(s)
                    s.close()
                    del message_queues[s]     
        for s in writable:
            try:
                next_msg = message_queues[s].get_nowait()
            except Queue.Empty:
                outputs.remove(s)
            else:
                s.sendall(next_msg)
        for s in exceptional:
            inputs.remove(s)
            if s in outputs:
                outputs.remove(s)
            s.close() 
            del message_queues[s]
