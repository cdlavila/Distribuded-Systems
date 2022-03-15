# Server program
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


IP = 'localhost'
PORT = 5004


def division(a, b):
    return a / b


def start():
    division_server = SimpleJSONRPCServer((IP, PORT))
    division_server.register_function(division)
    print(f"Division server listening on http://{IP}:{PORT}")
    division_server.serve_forever()


if __name__ == '__main__':
    start()
