from dnslib import DNSRecord, QTYPE, RR, A, DNSHeader
import socket
import socketserver

# Get the local IP address
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

# DNS server configuration
DOMAIN_TO_IP = {
    'cseseven.com': local_ip,
}

class DNSHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        try:
            request = DNSRecord.parse(data)
            qname = str(request.q.qname)
            qtype = QTYPE[request.q.qtype]
            
            print(f"Received request for: {qname} ({qtype})")

            # Prepare response
            reply = DNSRecord(DNSHeader(id=request.header.id, qr=1, aa=1, ra=1), q=request.q)
            
            if qname in DOMAIN_TO_IP:
                ip = DOMAIN_TO_IP[qname]
                reply.add_answer(RR(qname, QTYPE.A, rdata=A(ip), ttl=60))
                print(f"Responding with IP: {ip}")
            else:
                print("Domain not found")

            # Send the response back to the client
            socket.sendto(reply.pack(), self.client_address)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 53  # DNS typically uses port 53

    with socketserver.UDPServer((HOST, PORT), DNSHandler) as server:
        print("DNS Server is running...")
        server.serve_forever()
