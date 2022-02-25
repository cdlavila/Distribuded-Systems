import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 3000
BUFFER_SIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


operations = ['sum', 'subtraction', 'multiplication', 'division', 'power', 'logarithm']
print('\nAVAILABLE OPERATIONS:')
print('\n'.join(operations))

print('\nEnter de operation: ')
operation = input()
if operation not in operations:
    client.close()
    raise Exception('Invalid operation')

print('Enter the operator a: ')
a = input()
print('Enter the operator b: ')
b = input()

client.sendto(operation.encode('UTF-8'),(UDP_IP,UDP_PORT))
client.recvfrom(BUFFER_SIZE)
client.sendto(a.encode('UTF-8'),(UDP_IP,UDP_PORT))
client.recvfrom(BUFFER_SIZE)
client.sendto(b.encode('UTF-8'),(UDP_IP,UDP_PORT))
resultado , addr = client.recvfrom(1024)
result = resultado.decode("UTF-8")
print ("El resultado es: ", result, "recibido de:", addr)
client.close()
