# Sockets with JSON and XML

This repository contains socket communication concepts worked at a low level using the Python socket library.

The example uses the TCP protocol:

The example is as follows:

We have 1 server running on localhost, this server can calculate whatever of the next arithmetic operations:

- sum
- subtraction
- multiplication
- division
- power
- logarithm

The messages between client and server are sent in 2 differents ways:
- json
- xml

The client send an operation, an operator a and an operator b to the server, and the server send the operation result to the client.
