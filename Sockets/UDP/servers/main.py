import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 3000  # (1024, 65535]
BUFFER_SIZE = 1024
SERVERS = {'sum': ('127.0.0.1', 5001), 'subtraction': ('127.0.0.1', 5002), 'multiplication': ('127.0.0.1', 5003),
           'division': ('127.0.0.1', 5004), 'power': ('127.0.0.1', 5005), 'logarithm': ('127.0.0.1', 5006)}

main_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
main_server.bind((UDP_IP, UDP_PORT))

print(f'Main server listening on {UDP_IP}:{UDP_PORT}')

operation, address = main_server.recvfrom(BUFFER_SIZE)
if not operation:
    raise Exception('Error with the operation')
print("Address: ", address[0])
print("Port: ", address[1])
print("\nOperation received: ", operation.decode("UTF-8"))
main_server.sendto("Received".encode("UTF-8"), (address[0], address[1]))

a, address = main_server.recvfrom(BUFFER_SIZE)
if not a:
    raise Exception('Error with the operator a')
print("Operator received (a): ", a.decode("UTF-8"))
main_server.sendto("Received".encode("UTF-8"), (address[0], address[1]))

b, address = main_server.recvfrom(BUFFER_SIZE)
if not b:
    raise Exception('Error with the operator b')
print("Operator received (b): ", b.decode("UTF-8"))

sum_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sum_server.sendto(a, SERVERS[operation.decode("UTF-8")])
data = sum_server.recvfrom(BUFFER_SIZE)
sum_server.sendto(b, SERVERS[operation.decode("UTF-8")])
result, address2 = sum_server.recvfrom(BUFFER_SIZE)
sum_server.close()

print("Result sent: ", result.decode("UTF-8"))
main_server.sendto(result, (address[0], address[1]))
main_server.close()
