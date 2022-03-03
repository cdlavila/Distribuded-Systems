# Sockets
This repository contains socket communication concepts worked at a low level using the Python socket library.

We have the same example of socket communication with two different protocols:
- TCP
- UDP

The example is as follows:

We have 7 servers running on localhost, all of them on different ports:
- main
- sum
- subtraction
- multiplication
- division
- power
- logarithm

And, we have a client that connects to the main server to request an operation between two numbers, the main server is responsible for connecting to the correct server that can solve that operation, for example, if the operation is a sum, then the main server has to connect to the sum server, send it the numbers and get the result, then the main server has to send this result to the client and this is responsible for displaying the result.
