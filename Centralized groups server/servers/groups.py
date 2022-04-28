import socket
import json
import sys
import threading

TCP_IP = 'localhost'
TCP_PORT = 3000
BUFFER_SIZE = 1024

MENU = [
    {'option': '1', 'action': 'List groups'},
    {'option': '2', 'action': 'Join a group'},
    {'option': '3', 'action': 'Leave a group'},
    {'option': '4', 'action': 'Create a group'},
    {'option': '5', 'action': 'Delete a group'},
    {'option': '6', 'action': 'Exit'}
]

GROUPS = [
    {'name': 'sum', 'members': [], 'leader': None},
    {'name': 'subtraction', 'members': [], 'leader': None},
    {'name': 'multiplication', 'members': [], 'leader': None},
    {'name': 'division', 'members': [], 'leader': None},
    {'name': 'power', 'members': [], 'leader': None},
    {'name': 'logarithm', 'members': [], 'leader': None}
]


# List all groups
def list_groups():
    return {'message': 'Groups list', 'data': GROUPS}


# Join a member to a group
def join_group(group_name, ip, port):
    for group in GROUPS:
        if group['name'] == group_name:
            if (ip, port) not in group['members']:
                group['members'].append((ip, port))
                if len(group['members']) > 1:
                    return {'message': f'You have successfully joined to the group {group_name}', 'data': None}
                else:
                    group['leader'] = (ip, port)
                    return {'message': f'You have successfully joined to the group {group_name} and now you are the '
                                       'leader', 'data': None}
            else:
                return {'message': f'You already belong to the group {group_name}', 'data': None}

    return {'message': f'The group {group_name} does not exist, you can create it', 'data': None}


# Leave a member from a group
def leave_group(group_name, ip, port):
    for group in GROUPS:
        if group['name'] == group_name:
            if (ip, port) in group['members']:
                group['members'].remove((ip, port))
                if group['leader'] == (ip, port):
                    group['leader'] = None
                return {'message': f'You have successfully left the group {group_name}', 'data': None}
            else:
                return {'message': f'You do not belong to the group {group_name}', 'data': None}

    return {'message': f'The group {group_name} does not exist', 'data': None}


# Create a group
def create_group(group_name, ip, port):
    for group in GROUPS:
        if group['name'] == group_name:
            return {'message': f'The group {group_name} already exists, you can join it', 'data': None}

    GROUPS.append({'name': group_name, 'members': [(ip, port)], 'leader': (ip, port)})
    return {'message': f'The group {group_name} was successfully created and you are the leader', 'data': None}


# Remove a group
def remove_group(group_name):
    for group in GROUPS:
        if group['name'] == group_name:
            GROUPS.remove(group)
            return {'message': f'The group {group_name} was successfully removed', 'data': None}

    return {'message': f'The group {group_name} does not exist', 'data': None}


# handler
def handler(connection, address):
    data_received = json.loads(connection.recv(BUFFER_SIZE).decode('UTF-8'))
    if not data_received:
        sys.exit()
    print('Message received: ', data_received['message'])
    print('Menu sent')
    connection.send(json.dumps({'message': 'GROUPS SERVER MENU', 'data': MENU}).encode('UTF-8'))

    data_received = json.loads(connection.recv(BUFFER_SIZE).decode('UTF-8'))
    print('\nOption received: ', data_received['option'])
    if data_received['option'] == '1':
        data_to_send = list_groups()
    elif data_received['option'] == '2':
        data_to_send = join_group(data_received['group_name'], address[0], address[1])
    elif data_received['option'] == '3':
        data_to_send = leave_group(data_received['group_name'], address[0], address[1])
    elif data_received['option'] == '4':
        data_to_send = create_group(data_received['group_name'], address[0], address[1])
    elif data_received['option'] == '5':
        data_to_send = remove_group(data_received['group_name'])
    else:
        data_to_send = {'message': 'The selected option is not valid', 'data': None}

    connection.send(json.dumps(data_to_send).encode('UTF-8'))
    connection.close()


# Start group server
def start_groups_server():
    groups_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    groups_server.bind((TCP_IP, TCP_PORT))
    groups_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    groups_server.listen(5)
    print(f'Groups server listening on {TCP_IP}:{TCP_PORT}')

    while 1:
        connection, address = groups_server.accept()
        print('\nClient address: ', address[0])
        print('Client port: ', address[1])
        thread1 = threading.Thread(target=handler, args=(connection, address))
        thread1.start()


if __name__ == '__main__':
    start_groups_server()
