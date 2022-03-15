import socket
from dict2xml import dict2xml
import xmltodict

TCP_IP = '127.0.0.1'
TCP_PORT = 3000
BUFFER_SIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((TCP_IP, TCP_PORT))

operations = ['sum', 'subtraction', 'multiplication', 'division', 'power', 'logarithm']
print('\nAVAILABLE OPERATIONS:')
print('\n'.join(operations))

print('\nEnter the operation: ')
operation = input()
if operation not in operations:
    client.close()
    raise Exception('Invalid operation')

print('Enter the operator a: ')
a = input()
print('Enter the operator b: ')
b = input()

data = dict2xml({'a': a, 'b': b, 'operation': operation}, wrap='data')
client.send(data.encode('UTF-8'))
result = xmltodict.parse((client.recv(BUFFER_SIZE).decode('UTF-8')))['data']
client.close()

print('The result is:', result['result'])
