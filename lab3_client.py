#Client-Side Implementation:-------


import socket

def client_program():
    host = 'localhost' # Get the hostname of the server
    port = 5000  # Port to connect to

    # Create a client socket instance
    client_socket = socket.socket()

    # Connect to the server
    client_socket.connect((host, port))

    message = input("Enter message to send to server: ")  # Get user input

    while message.lower().strip() != 'bye':
        # Send message to the server
        client_socket.send(message.encode())

        # Receive response from the server
        data = client_socket.recv(1024).decode()
        print(f"Received from server: {data}")

        # Continue communication
        message = input("Enter message to send to server: ")

    # Close the connection
    client_socket.close()

if __name__ == '__main__':
    client_program()
