#client_side implement:----
import socket

def send_messages(server_host='127.0.0.1', server_port=6100):
    """Function to send messages to the server."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    while True:
        message = input("Enter message to send (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        client_socket.sendall(message.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Server response: {response}")

    client_socket.close()


if __name__ == "__main__":
    send_messages()




