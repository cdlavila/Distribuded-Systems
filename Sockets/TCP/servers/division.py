import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5004  # (1024, 65535]
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(5)
print(f'Division server listening on {TCP_IP}:{TCP_PORT}')

while 1:
    conn, address = s.accept()
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

    division = int(a) / int(b)
    print("Result sent: ", division)
    conn.send(str(division).encode("UTF-8"))

    conn.close()
