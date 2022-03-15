from jsonrpclib import Server


def start():
    connection = Server('http://localhost:3000')

    operations = ['sum', 'subtraction', 'multiplication', 'division', 'power', 'logarithm']
    print('\nAVAILABLE OPERATIONS:')
    print('\n'.join(operations))

    print('\nEnter de operation: ')
    operation = input()
    if operation not in operations:
        raise Exception('Invalid operation')

    print('Enter the operator a: ')
    a = int(input())
    print('Enter the operator b: ')
    b = int(input())
    print('The result is:', connection.request_operation(operation, a, b))


if __name__ == '__main__':
    start()
