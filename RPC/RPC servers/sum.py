# Server program
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


IP = 'localhost'
PORT = 5001


def sum(a, b):
    return a + b


def start():
    sum_server = SimpleJSONRPCServer((IP, PORT))
    sum_server.register_function(sum)
    print(f"Sum server listening on http://{IP}:{PORT}")
    sum_server.serve_forever()


if __name__ == '__main__':
    start()
