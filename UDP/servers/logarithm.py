import socket
import math
UDP_IP = '127.0.0.1'
UDP_PORT = 5006  # (1024, 65535]
BUFFER_SIZE = 1024

log_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
log_server.bind((UDP_IP,UDP_PORT))
print(f'Sum server listening on {UDP_IP}:{UDP_PORT}')
data, addr = log_server.recvfrom(1024)
print ("Dato 1:", data.decode("UTF-8"), "recibido de:", addr)
log_server.sendto("recibido".encode("UTF-8"),(addr[0],addr[1]))
data2, addr = log_server.recvfrom(1024)
print ("Dato 2:", data2.decode("UTF-8"), "recibido de:", addr)
a = int(data.decode("UTF-8"))
b = int(data2.decode("UTF-8"))
log = math.log(b, a)
log_server.sendto(str(log).encode("UTF-8"),(addr[0],addr[1]))
print ("Resultado enviado: ", log)
log_server.close()
