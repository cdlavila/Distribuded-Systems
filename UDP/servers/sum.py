import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 5001  # (1024, 65535]
BUFFER_SIZE = 1024

sum_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sum_server.bind((UDP_IP,UDP_PORT))
print(f'Sum server listening on {UDP_IP}:{UDP_PORT}')
data, addr = sum_server.recvfrom(1024)
print ("Dato 1:", data.decode("UTF-8"), "recibido de:", addr)
sum_server.sendto("recibido".encode("UTF-8"),(addr[0],addr[1]))
data2, addr = sum_server.recvfrom(1024)
print ("Dato 2:", data2.decode("UTF-8"), "recibido de:", addr)
a = int(data.decode("UTF-8"))
b = int(data2.decode("UTF-8"))
suma = a + b
sum_server.sendto(str(suma).encode("UTF-8"),(addr[0],addr[1]))
print ("Resultado enviado: ", suma)
sum_server.close()
