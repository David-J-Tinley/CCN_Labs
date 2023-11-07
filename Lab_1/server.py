#!/usr/bin/python3

###############################################################################
# server.py
#
# Lab 1
# David J Tinley
# 09/28/2023
#
# Objective - Develop a web server that handles one HTTP request at a time.
###############################################################################

import socket

PORT = 8080  # use port 8080
HOST = "0.0.0.0"  # listen for all address's

print(f"Server listening on http://{HOST}:{PORT}")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

while True:
    client_socket = None  # Used to suppress Pylance linting error
    print("Waiting...")
    try:
        client_socket, client_address = server_socket.accept()
        print(f"Request received from {client_address}")

        file_request = client_socket.recv(1024).decode("utf-8")
        file_name = file_request.split()[1]
        file = open(file_name[1:])

        output_data = file.read()
        header_response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n"
        client_socket.sendall(header_response.encode("utf-8"))

        for i in range(0, len(output_data)):
            client_socket.send(output_data[i].encode())

        client_socket.send("\r\n".encode())
        client_socket.close()

    except FileNotFoundError:
        if client_socket is not None:  # Used to suppress Pylance linting error
            client_socket.sendall(
                b"HTTP/1.1 404 Not Found\nContent-Type: text/html\n\nFile Not Found"
            )
            client_socket.close()

    finally:
        if client_socket is not None:  # Used to suppress Pylance linting error
            client_socket.close()
