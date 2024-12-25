import socket

# DNS table for managing custom domain
dns_table = {
    "www.cseseven.com": "192.168.1.100"  # IP address mapped to the domain
}

# Function to handle DNS queries
def handle_dns_request(data):
    try:
        domain = data.decode().strip()  # Decode the query
        print(f"Received DNS query for: {domain}")

        # Check for the domain in the DNS table
        if domain in dns_table:
            return dns_table[domain]
        else:
            return "Domain not found"
    except Exception as e:
        print(f"Error processing query: {e}")
        return "Error processing request"

# Function to start the DNS server
def start_dns_server():
    server_ip, port = "0.0.0.0", 5354  # Bind to all interfaces for mobile accessibility
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_ip, port))
    print(f"DNS Server running on {server_ip}:{port}")

    try:
        while True:
            # Receive query from client
            data, client_address = server_socket.recvfrom(1024)
            response = handle_dns_request(data)

            # Send the response back to client
            server_socket.sendto(response.encode(), client_address)
            print(f"Sent response to {client_address}: {response}")
    except KeyboardInterrupt:
        print("\nDNS Server shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_dns_server()
