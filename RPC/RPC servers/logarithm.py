# Server program
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
import math


IP = 'localhost'
PORT = 5006


def logarithm(a, b):
    return math.log(b, a)


def start():
    logarithm_server = SimpleJSONRPCServer((IP, PORT))
    logarithm_server.register_function(logarithm)
    print(f"Logarithm server listening on http://{IP}:{PORT}")
    logarithm_server.serve_forever()


if __name__ == '__main__':
    start()
