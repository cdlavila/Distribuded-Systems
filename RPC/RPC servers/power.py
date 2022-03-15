# Server program
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


IP = 'localhost'
PORT = 5005


def power(a, b):
    return a ** b


def start():
    power_server = SimpleJSONRPCServer((IP, PORT))
    power_server.register_function(power)
    print(f"Power server listening on http://{IP}:{PORT}")
    power_server.serve_forever()


if __name__ == '__main__':
    start()
