# Server program
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from jsonrpclib import Server

IP = 'localhost'
PORT = 3000


class Operations:
    connection = None

    def __init__(self):
        self.connection = None

    def request_operation(self, operation, a, b):
        operations = {
            'sum': self.sum(a, b),
            'subtraction': self.subtraction(a, b),
            'multiplication': self.multiplication(a, b),
            'division': self.division(a, b),
            'power': self.power(a, b),
            'logarithm': self.logarithm(a, b)
        }
        return operations[operation]

    def sum(self, a, b):
        self.connection = Server('http://localhost:5001')
        return self.connection.sum(a, b)

    def subtraction(self, a, b):
        self.connection = Server('http://localhost:5002')
        return self.connection.subtraction(a, b)

    def multiplication(self, a, b):
        self.connection = Server('http://localhost:5003')
        return self.connection.multiplication(a, b)

    def division(self, a, b):
        self.connection = Server('http://localhost:5004')
        return self.connection.division(a, b)

    def power(self, a, b):
        self.connection = Server('http://localhost:5005')
        return self.connection.power(a, b)

    def logarithm(self, a, b):
        self.connection = Server('http://localhost:5006')
        return self.connection.logarithm(a, b)


def start():
    main_server = SimpleJSONRPCServer((IP, PORT))
    main_server.register_instance(Operations())
    print(f"Main server listening on http://{IP}:{PORT}")
    main_server.serve_forever()


if __name__ == '__main__':
    start()
