# import http.server
# import socketserver

# PORT = 8002

# # Create a handler to serve the files
# Handler = http.server.SimpleHTTPRequestHandler

# # Set up the server to listen on localhost (127.0.0.1)
# with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
#     print(f"Serving on localhost at port {PORT}")
#     httpd.serve_forever()

from http.server import HTTPServer, SimpleHTTPRequestHandler

def run_localhost_server(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('127.0.0.1', 8000)
    httpd = server_class(server_address, handler_class)
    print("Serving HTTP on Localhost(127.0.0.1) at port 8000...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_localhost_server()