import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 3000  # (1024, 65535]
BUFFER_SIZE = 1024

main_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
main_server.bind((UDP_IP,UDP_PORT))
print(f'Main server listening on {UDP_IP}:{UDP_PORT}')
operation, address = main_server.recvfrom(BUFFER_SIZE)
print ("Operation:", operation.decode("UTF-8"), "reciv: ", address)
main_server.sendto("Received".encode("UTF-8"),(address[0],address[1]))
data, addr = main_server.recvfrom(1024)
print ("Dato 1:", data.decode("UTF-8"), "recibido de:", addr)
main_server.sendto("recibido".encode("UTF-8"),(addr[0],addr[1]))
data2, addr = main_server.recvfrom(1024)
print ("Dato 2:", data2.decode("UTF-8"), "recibido de:", addr)
a = data.decode("UTF-8")
b = data2.decode("UTF-8")

if operation.decode("UTF-8") == 'sum':
    operation_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    operation_server.sendto(a.encode('UTF-8'), (UDP_IP, 5001))
    operation_server.recvfrom(BUFFER_SIZE)
    operation_server.sendto(b.encode('UTF-8'), (UDP_IP, 5001))
    result , address = operation_server.recvfrom(1024)
    print ("El resultado es:", result.decode("UTF-8"), "recibido de:", address)
    main_server.sendto(result,(addr[0],addr[1]))
    main_server.close()
else:
    if operation.decode("UTF-8") == 'subtraction':
        operation_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        operation_server.sendto(a.encode('UTF-8'), (UDP_IP, 5002))
        operation_server.recvfrom(BUFFER_SIZE)
        operation_server.sendto(b.encode('UTF-8'), (UDP_IP, 5002))
        result , address = operation_server.recvfrom(1024)
        print ("El resultado es:", result.decode("UTF-8"), "recibido de:", address)
        main_server.sendto(result,(addr[0],addr[1]))
        main_server.close()
    else:
        if operation.decode("UTF-8") == 'multiplication':
            operation_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            operation_server.sendto(a.encode('UTF-8'), (UDP_IP, 5003))
            operation_server.recvfrom(BUFFER_SIZE)
            operation_server.sendto(b.encode('UTF-8'), (UDP_IP, 5003))
            result , address = operation_server.recvfrom(1024)
            print ("El resultado es:", result.decode("UTF-8"), "recibido de:", address)
            main_server.sendto(result,(addr[0],addr[1]))
            main_server.close()
        else:
            if operation.decode("UTF-8") == 'division':
                operation_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                operation_server.sendto(a.encode('UTF-8'), (UDP_IP, 5004))
                operation_server.recvfrom(BUFFER_SIZE)
                operation_server.sendto(b.encode('UTF-8'), (UDP_IP, 5004))
                result , address = operation_server.recvfrom(1024)
                print ("El resultado es:", result.decode("UTF-8"), "recibido de:", address)
                main_server.sendto(result,(addr[0],addr[1]))
                main_server.close()
            else:
                if operation.decode("UTF-8") == 'power':
                    operation_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    operation_server.sendto(a.encode('UTF-8'), (UDP_IP, 5005))
                    operation_server.recvfrom(BUFFER_SIZE)
                    operation_server.sendto(b.encode('UTF-8'), (UDP_IP, 5005))
                    result , address = operation_server.recvfrom(1024)
                    print ("El resultado es:", result.decode("UTF-8"), "recibido de:", address)
                    main_server.sendto(result,(addr[0],addr[1]))
                    main_server.close()
                else: 
                    if operation.decode("UTF-8") == 'logarithm':
                        operation_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        operation_server.sendto(a.encode('UTF-8'), (UDP_IP, 5006))
                        operation_server.recvfrom(BUFFER_SIZE)
                        operation_server.sendto(b.encode('UTF-8'), (UDP_IP, 5006))
                        result , address = operation_server.recvfrom(1024)
                        print ("El resultado es:", result.decode("UTF-8"), "recibido de:", address)
                        main_server.sendto(result,(addr[0],addr[1]))
                        main_server.close()

