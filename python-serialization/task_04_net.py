#!/usr/bin/python3

"""
task_04_net.py
Serialization in network communication
"""

import socket
import json


def start_server():
    """
    start_server - Set up server using socket library
    Return: Void
    """
    # --- Create socket ---
    # AF_INET = IPv4
    # SOCK_STREAM = TCP (reliable server)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # --- Link socket to an adress and a port ---
    host = "127.0.0.1" # Local adress
    port = 12345
    server_socket.bind((host, port))

    # --- Open socket to listen mode ---
    server_socket.listen(1) # 1 = max waiting connexion
    print("Server listening on {}:{}".format(host, port))

    # --- Accept entering connexion
    client_socket, client_adress = server_socket.accept()
    print("Connected with {}".format(client_adress))

    # --- Receive data ---
    data = client_socket.recv(1024) # 1024 = max octets

    # --- Convert bytes in dictionary ---
    data_str = data.decode("utf-8") # Convert bytes in string
    data_dict = json.loads(data_str) # Deserialiaze json string to dictionary

    # --- Display dict ---
    print("Dictionary : ", data_dict)

    # --- Close connexion ---
    client_socket.close()
    server_socket.close()


def send_data(dictionary):
    """
    send_data - Function that acts as the client
    @dictionary: Dictionary send by the client
    Return: Void
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 12345

    client_socket.connect((host, port))

    data_str = json.dumps(dictionary)

    client_socket.send(data_str.encode("utf-8"))

    client_socket.close()
