import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 5003  # (1024, 65535]
BUFFER_SIZE = 1024

mul_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mul_server.bind((UDP_IP,UDP_PORT))
print(f'Sum server listening on {UDP_IP}:{UDP_PORT}')
data, addr = mul_server.recvfrom(1024)
print ("Dato 1:", data.decode("UTF-8"), "recibido de:", addr)
mul_server.sendto("recibido".encode("UTF-8"),(addr[0],addr[1]))
data2, addr = mul_server.recvfrom(1024)
print ("Dato 2:", data2.decode("UTF-8"), "recibido de:", addr)
a = int(data.decode("UTF-8"))
b = int(data2.decode("UTF-8"))
mul = a * b
mul_server.sendto(str(mul).encode("UTF-8"),(addr[0],addr[1]))
print ("Resultado enviado: ", mul)
mul_server.close()
