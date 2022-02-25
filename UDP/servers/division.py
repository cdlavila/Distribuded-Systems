import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 5004  # (1024, 65535]
BUFFER_SIZE = 1024

division_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
division_server.bind((UDP_IP, UDP_PORT))
print(f'Division server listening on {UDP_IP}:{UDP_PORT}')
a, address = division_server.recvfrom(BUFFER_SIZE)
if not a:
    raise Exception('Error with the operator a')
print("Address: ", address[0])
print("Port: ", address[1])
print("\nOperator received (a): ", a.decode("UTF-8"))
division_server.sendto("Received".encode("UTF-8"), (address[0], address[1]))

b, address = division_server.recvfrom(BUFFER_SIZE)
if not b:
    raise Exception('Error with the operator b')
print("Operator received (b): ", b.decode("UTF-8"))

division = int(a) / int(b)
print("Result sent: ", division)
division_server.sendto(str(division).encode("UTF-8"), (address[0], address[1]))

division_server.close()
