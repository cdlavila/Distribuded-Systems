import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 3000  # (1024, 65535]
BUFFER_SIZE = 1024
SERVERS = {'sum': ('127.0.0.1', 5001), 'subtraction': ('127.0.0.1', 5002), 'multiplication': ('127.0.0.1', 5003),
           'division': ('127.0.0.1', 5004), 'power': ('127.0.0.1', 5005), 'logarithm': ('127.0.0.1', 5006)}

main_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_server.bind((TCP_IP, TCP_PORT))
main_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
main_server.listen(5)
print(f'Main server listening on {TCP_IP}:{TCP_PORT}')

while 1:
    conn, address = main_server.accept()
    operation = conn.recv(BUFFER_SIZE).decode("UTF-8")
    if not operation:
        break
    print("Address: ", address[0])
    print("Port: ", address[1])
    print("\nOperation received: ", operation)
    conn.send("Received".encode("UTF-8"))

    a = conn.recv(BUFFER_SIZE).decode("UTF-8")
    if not a:
        break
    print("Operator received (a): ", a)
    conn.send("Received".encode("UTF-8"))

    b = conn.recv(BUFFER_SIZE).decode("UTF-8")
    if not b:
        break
    print("Operator received (b): ", b)

    operation_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    operation_server.connect(SERVERS[operation])
    operation_server.send(a.encode('UTF-8'))
    operation_server.recv(BUFFER_SIZE).decode('UTF-8')
    operation_server.send(b.encode('UTF-8'))
    result = operation_server.recv(BUFFER_SIZE).decode('UTF-8')
    operation_server.close()
    print("Result sent: ", result)
    conn.send(str(result).encode("UTF-8"))

    conn.close()
