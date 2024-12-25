# import http.server
# import socketserver

# PORT = 8001

# Handler = http.server.SimpleHTTPRequestHandler

# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print(f"Serving at port {PORT}")
#     print("successfully build server")
#     httpd.serve_forever()

from http.server import HTTPServer, SimpleHTTPRequestHandler

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('0.0.0.0', 8000)
    httpd = server_class(server_address, handler_class)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()