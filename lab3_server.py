import socket

def server_program():
    # Get the hostname of the machine
    host = 'localhost'
    port = 5000  # Port for listening

    # Create a server socket instance
    server_socket = socket.socket()

    # Bind the host address and port together
    server_socket.bind((host, port))

    # Listen for incoming connections (allow up to 2 connections)
    server_socket.listen(2)
    print(f"Server is listening on {host}:{port}")

    while True:
        # Accept connection from client
        conn, address = server_socket.accept()
        print(f"Connection from {address} has been established.")

        # Receive data from client
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break  # If no data is received, exit the loop
            print(f"Received from client: {data}")

            # Send a response back to the client
            data = input('Enter response to client: ')
            conn.send(data.encode())  # Send response to client

        # Close the connection
        conn.close()

if __name__ == '__main__':
    server_program()



