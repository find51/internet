import socket

# Custom DNS table for multiple domains
dns_table = {
    "myapp.local": "192.168.1.10",
    "project.test": "192.168.1.20",
    "service.local": "192.168.1.30",
    "example.local": "127.0.0.1"
}

# Function to handle incoming DNS requests
def handle_dns_request(data):
    try:
        domain = data.decode().strip()  # Decode incoming request
        print(f"Received DNS query for domain: {domain}")

        # Check for domain in the DNS table
        if domain in dns_table:
            return dns_table[domain]  # Return IP address
        else:
            return "Domain not found"  # Return error if domain is not found
    except Exception as e:
        print(f"Error handling request: {e}")
        return "Error processing request"

# Function to start the DNS server
def start_dns_server():
    host, port = "127.0.0.1", 5354  # Localhost and port 5354
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"Local DNS Server running on {host}:{port}")

    try:
        while True:
            # Receive query from the client
            data, client_address = server_socket.recvfrom(1024)
            response = handle_dns_request(data)

            # Send the response back to the client
            server_socket.sendto(response.encode(), client_address)
            print(f"Sent response to {client_address}: {response}")
    except KeyboardInterrupt:
        print("\nDNS Server shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_dns_server()
