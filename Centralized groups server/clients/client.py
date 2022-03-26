import socket
import json

TCP_IP = '127.0.0.1'
TCP_PORT = 3000
BUFFER_SIZE = 1024


def print_menu(menu, message):
    print(f'\n{message}:')
    print("{:<8} {:<8}".format('Option', 'Action'))
    for element in menu:
        print("{:<8} {:<8}".format('  ' + element['option'], element['action']))


def print_groups(groups):
    print("{:<15} {:<60} {:<10}".format('Name', 'Members', 'Leader'))
    for group in groups:
        print("{:<15} {:<60} {:<10}".format(group['name'], str(group['members']), str(group['leader'])))


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((TCP_IP, TCP_PORT))

    client.send(json.dumps({'message': 'Hello'}).encode('UTF-8'))
    data_received = json.loads(client.recv(BUFFER_SIZE).decode('UTF-8'))
    print_menu(data_received['data'], data_received['message'])

    # Send data
    option = input('\nEnter the option: ')
    data_to_send = {'option': option}
    if option in ['2', '3', '4', '5']:
        group_name = input('Enter the group name: ')
        data_to_send['group_name'] = group_name
    client.send(json.dumps(data_to_send).encode('UTF-8'))

    #  Receive data
    data_received = json.loads(client.recv(BUFFER_SIZE).decode('UTF-8'))

    # Print data
    if option == '1':
        print('\n' + data_received['message'])
        print_groups(data_received['data'])
    else:
        print(data_received['message'])

    client.close()


if __name__ == '__main__':
    start_client()
