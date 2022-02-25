import socket
import math
UDP_IP = '127.0.0.1'
UDP_PORT = 5005  # (1024, 65535]
BUFFER_SIZE = 1024

pow_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
pow_server.bind((UDP_IP,UDP_PORT))
print(f'Sum server listening on {UDP_IP}:{UDP_PORT}')
data, addr = pow_server.recvfrom(1024)
print ("Dato 1:", data.decode("UTF-8"), "recibido de:", addr)
pow_server.sendto("recibido".encode("UTF-8"),(addr[0],addr[1]))
data2, addr = pow_server.recvfrom(1024)
print ("Dato 2:", data2.decode("UTF-8"), "recibido de:", addr)
a = int(data.decode("UTF-8"))
b = int(data2.decode("UTF-8"))
pow = a **  b
pow_server.sendto(str(pow).encode("UTF-8"),(addr[0],addr[1]))
print ("Resultado enviado: ", pow)
pow_server.close()

