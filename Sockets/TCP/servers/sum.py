import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5001  # (1024, 65535]
BUFFER_SIZE = 1024

sum_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sum_server.bind((TCP_IP, TCP_PORT))
sum_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sum_server.listen(5)
print(f'Sum server listening on {TCP_IP}:{TCP_PORT}')

while 1:
    conn, address = sum_server.accept()
    a = conn.recv(BUFFER_SIZE).decode("UTF-8")
    if not a:
        break
    print("Address: ", address[0])
    print("Port: ", address[1])
    print("\nOperator received (a): ", a)
    conn.send("Received".encode("UTF-8"))

    b = conn.recv(BUFFER_SIZE).decode("UTF-8")
    if not b:
        break
    print("Operator received (b): ", b)

    sum = int(a) + int(b)
    print("Result sent: ", sum)
    conn.send(str(sum).encode("UTF-8"))

    conn.close()
