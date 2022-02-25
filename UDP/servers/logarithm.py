import math
import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 5006  # (1024, 65535]
BUFFER_SIZE = 1024

logarithm_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
logarithm_server.bind((UDP_IP, UDP_PORT))
print(f'Logarithm server listening on {UDP_IP}:{UDP_PORT}')
a, address = logarithm_server.recvfrom(BUFFER_SIZE)
if not a:
    raise Exception('Error with the operator a')
print("Address: ", address[0])
print("Port: ", address[1])
print("\nOperator received (a): ", a.decode("UTF-8"))
logarithm_server.sendto("Received".encode("UTF-8"), (address[0], address[1]))

b, address = logarithm_server.recvfrom(BUFFER_SIZE)
if not b:
    raise Exception('Error with the operator b')
print("Operator received (b): ", b.decode("UTF-8"))

logarithm = math.log(int(b), int(a))
print("Result sent: ", logarithm)
logarithm_server.sendto(str(logarithm).encode("UTF-8"), (address[0], address[1]))

logarithm_server.close()
