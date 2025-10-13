import http.server
import socketserver
import os
import sys

PORT = 8000
DIRECTORY = "pages"  # Serve files from the 'pages' directory

# Verify the pages directory exists
if not os.path.isdir(DIRECTORY):
    print(f"Error: Directory '{DIRECTORY}' does not exist.")
    sys.exit(1)

# Change to the pages directory for serving
try:
    os.chdir(DIRECTORY)
    print(f"Changed to directory: {os.getcwd()}")
except OSError as e:
    print(f"Error: Could not change to directory '{DIRECTORY}': {e}")
    sys.exit(1)

# Set up the server
Handler = http.server.SimpleHTTPRequestHandler

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving {DIRECTORY} at http://localhost:{PORT}")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped by user (Ctrl+C).")
    httpd.server_close()
except OSError as e:
    print(f"Error: Could not start server: {e}")
    sys.exit(1)
