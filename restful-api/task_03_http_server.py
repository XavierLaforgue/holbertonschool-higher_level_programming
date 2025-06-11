#!/usr/bin/python3
"""
Module Name: task_03_http_server.

Contains setup of a simple http server.
"""
import http.server
import json

class my_handler(http.server.BaseHTTPRequestHandler):
    """Defines http request handler."""
    def do_GET(self):
        """Handle GET requests."""
        print(f"Received GET request for: {self.path}")
        if self.path == "/":
            self.send_response(200,
                               message="Message for GET request OK")
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!\n")
        elif self.path == "/data":
            dataset = {
                "name": "John",
                "age": 30,
                "city": "New York"
                }
            dataset_json = json.dumps(dataset).encode("utf-8")
            self.send_response(200,
                message="Message fo GET /data request OK")
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(dataset_json +b"\n")
        elif self.path == "/status":
            self.send_response(200, message="OK for GET /status")
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK\n")
        elif self.path == "/info":
            info_dict={
                "version": "1.0",
                "description": "A simple API built with http.server"
                }
            info_json = json.dumps(info_dict)
            self.send_response(200,
                message="Message fo GET /info request OK")
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(info_json.encode("utf-8") + b"\n")
        else:
            self.send_response(404, message="Personalized Not Found")
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found: The requested endpoint"
                             b" is undefined\n")


    def do_POST(self):
        """Handle POST requests."""
        print(f"Received POST request for: {self.path}")
        self.send_response(200, message="Default: OK. Some personalized message")
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Is it doing POST?\n")
        


def run(server_class=http.server.HTTPServer,
    handler_class=my_handler):
        """Does something."""
        port = 8000
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        print(f"Server running at http://localhost:{port}...")
        try:
            httpd.serve_forever()
        except:
            print("\n Server is shutting down.")
            httpd.server_close()


if __name__ == "__main__":
    run()
