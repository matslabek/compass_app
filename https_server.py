#!/usr/bin/env python3
import http.server
import ssl
import os

# change to the directory where this script is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# create HTTP server
server_address = ('', 8443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# wrap with SSL
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('cert.pem', 'key.pem')
httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

print(f"Serving HTTPS on https://localhost:8443")
print(f"Note: You'll need to accept the self-signed certificate warning in your browser")
httpd.serve_forever()

