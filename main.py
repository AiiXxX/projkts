import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = "pages"  # Serve files from the 'pages' directory

# Change to the pages directory for serving
os.chdir(DIRECTORY)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving {DIRECTORY} at http://localhost:{PORT}")
    httpd.serve_forever()
