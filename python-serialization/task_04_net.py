#!/usr/bin/python3

"""
task_04_net.py
Serialization in network communication
"""

import socket
import json


def start_server(host="127.0.0.1", port=12345):
    """
    start_server - Set up server using socket library
    @host: Default host address
    @port: Default port
    Return: Void
    """
    # Create socket
    # AF_INET = IPv4
    # SOCK_STREAM = TCP (reliable server)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Link socket to an adress and a port
        server_socket.bind((host, port))
        # Open socket to listen mode
        server_socket.listen()
        print("Server listening on {}:{}".format(host, port))
        # Accept entering connexion
        client_socket, client_adress = server_socket.accept()
        with client_socket:
            print("Connected with {}".format(client_adress))
            # Receive data
            data = client_socket.recv(1024) # 1024 = max octets
            if data:
                try:
                    # Deserialize json to dictionary
                    data_dict = json.loads(data.decode("utf-8"))
                    # Display dict
                    print("Dictionary : ", data_dict)
                except json.JSONDecodeError:
                    print("Failed to decode JSON data")


def send_data(data_dict, host="127.0.0.1", port=12345):
    """
    send_data - Function that acts as the client
    @data_dict: Dictionary send by the client
    @host: Default host address
    @port: Default port
    Return: Void
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            data_str = json.dumps(data_dict).encode("utf-8")
            client_socket.sendall(data_str)
            print("Data sent to the server successfully")
    except ConnectionRefusedError:
        print("Connection refused to the server")
    except Exception as error:
        print("An error occurred : {}".format(error))
