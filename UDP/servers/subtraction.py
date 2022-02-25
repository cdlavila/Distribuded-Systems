import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 5002  # (1024, 65535]
BUFFER_SIZE = 1024

subtraction_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
subtraction_server.bind((UDP_IP, UDP_PORT))
print(f'Subtraction server listening on {UDP_IP}:{UDP_PORT}')
a, address = subtraction_server.recvfrom(BUFFER_SIZE)
if not a:
    raise Exception('Error with the operator a')
print("Address: ", address[0])
print("Port: ", address[1])
print("\nOperator received (a): ", a.decode("UTF-8"))
subtraction_server.sendto("Received".encode("UTF-8"), (address[0], address[1]))

b, address = subtraction_server.recvfrom(BUFFER_SIZE)
if not b:
    raise Exception('Error with the operator b')
print("Operator received (b): ", b.decode("UTF-8"))

subtraction = int(a) - int(b)
print("Result sent: ", subtraction)
subtraction_server.sendto(str(subtraction).encode("UTF-8"), (address[0], address[1]))

subtraction_server.close()
