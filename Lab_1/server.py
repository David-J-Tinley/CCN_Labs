#!/usr/bin/python3

####################################
# server.py
#
# Lab 1
# David J Tinley
# 09/28/2023
#
# Objective - Develop a web server
# that handles one HTTP request at
# a time.
####################################

import socket
import sys


def Main():

    PORT = 8080.      # use port 8080
    HOST = '0.0.0.0'  # listen for all address's

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print(f"Server listening on http://{HOST}:{PORT}")

    while True:

        print("Waiting...")

        client_socket, client_address = server_socket.accept()

        try:
            print(f"Request recieved from {client_address}")

            file_request = client_socket.recv(1024).decode('utf-8')

            file_name = file_request.split()[1]

            file = open(file_name[1:])

            output_data = file.read()

            header_response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n"

            client_socket.sendall(header_response.encode('utf-8'))

            for i in range(0, len(output_data)):
                client_socket.send(output_data[i].encode())

            client_socket.send("\r\n".encode())

            client_socket.close()

        except IOError:
            client_socket.sendall(b"Error: File Not Found...")

        finally:
            client_socket.close()

    server_socket.close()
    sys.exit()


if __name__ == '__main__':
    Main()


#
#
#
#
#
#
#
#
#
#
