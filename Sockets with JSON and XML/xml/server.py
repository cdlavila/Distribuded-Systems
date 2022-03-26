import math
import socket
from dict2xml import dict2xml
import xmltodict


def calculate_operation(a, b, operation):
    if operation == 'sum':
        return a + b
    if operation == 'subtraction':
        return a - b
    if operation == 'multiplication':
        return a - b
    if operation == 'division':
        return a / b
    if operation == 'power':
        return a ** b
    if operation == 'logarithm':
        return math.log(b, a)


TCP_IP = 'localhost'
TCP_PORT = 3000
BUFFER_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((TCP_IP, TCP_PORT))
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.listen(5)
print(f'Server of arithmetic operations listening on {TCP_IP}:{TCP_PORT}')

while 1:
    conn, address = server.accept()
    data_received = xmltodict.parse(conn.recv(BUFFER_SIZE).decode("UTF-8"))['data']
    if not data_received:
        break
    print("\nClient address: ", address[0])
    print("Client port: ", address[1])
    print("\nOperation received: ", data_received['operation'])

    print("Operator received (a): ", data_received['a'])
    print("Operator received (b): ", data_received['b'])

    result = calculate_operation(int(data_received['a']), int(data_received['b']), data_received['operation'])
    print("Result sent: ", result)

    data_sent = dict2xml({'result': result}, wrap='data')
    conn.send(data_sent.encode("UTF-8"))

    conn.close()
