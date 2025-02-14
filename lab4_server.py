#server side implementation:----

import socket
import threading

def handle_client(client_socket):
    """Function to handle client connection."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received: {message}")
            client_socket.sendall(f"Echo: {message}".encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")
            break
    client_socket.close()


def start_server(host='127.0.0.1', port=6100):
    """Function to start the server."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    start_server()
