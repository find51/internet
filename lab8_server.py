import socket 
 
# DNS mapping table 
dns_table = { 
    "example.com": "93.184.216.34", 
    "google.com": "142.250.180.78", 
    "facebook.com": "157.240.22.35", 
    "localhost": "127.0.0.1" 
} 
 
# Function to handle incoming DNS queries 
def handle_dns_request(data):     
    try: 
        domain = data.decode().strip()  # Decode the request         
        print(f"Received query for domain: {domain}") 
            # Check for domain in DNS table         
        if domain in dns_table: 
                return dns_table[domain]         
        else: 
            return "Domain not found"     
    except Exception as e:         
        print(f"Error: {e}")         
        return "Error handling request" 
 
# Function to start the DNS server 
def start_dns_server(): 
    host, port = "127.0.0.1", 8053 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     
    server_socket.bind((host, port))     
    print(f"DNS Server running on {host}:{port}") 
    try:         
        while True: 
            # Receive query from client 
            data, client_address = server_socket.recvfrom(1024)             
            response = handle_dns_request(data) 
             
            # Send the response to the client 
            server_socket.sendto(response.encode(), client_address)             
            print(f"Sent response to {client_address}: {response}")     
    except KeyboardInterrupt: 
            print("\nDNS Server shutting down...")     
    finally:
        server_socket.close() 
 
# Start the DNS server 
if __name__ == "__main__": 
    start_dns_server() 
