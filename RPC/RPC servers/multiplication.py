# Server program
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


IP = 'localhost'
PORT = 5003


def multiplication(a, b):
    return a * b


def start():
    multiplication_server = SimpleJSONRPCServer((IP, PORT))
    multiplication_server.register_function(multiplication)
    print(f"Multiplication server listening on http://{IP}:{PORT}")
    multiplication_server.serve_forever()


if __name__ == '__main__':
    start()
