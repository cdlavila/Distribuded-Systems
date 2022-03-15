# Server program
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


IP = 'localhost'
PORT = 5002


def subtraction(a, b):
    return a - b


def start():
    subtraction_server = SimpleJSONRPCServer((IP, PORT))
    subtraction_server.register_function(subtraction)
    print(f"Subtraction server listening on http://{IP}:{PORT}")
    subtraction_server.serve_forever()


if __name__ == '__main__':
    start()
