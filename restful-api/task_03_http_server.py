#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

"""
task_03_http_server.py
API using http server
"""


class ServerHandler(BaseHTTPRequestHandler):
    """
    ServerHandler - Server Handler class
    """
    def do_GET(self):
        """
        do_GET - Get function
        Return: Void
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            message = "Hello, this is a simple API!"

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            message = json.dumps({
                "name": "John",
                "age": 30,
                "city": "New York"
                })

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            message = "OK"

        else:
            self.send_response(404, message="Not found")
            self.send_header("Content-type", "text/plain")
            self.end_header()
            message = "Endpoint not found"

        self.wfile.write(bytes(message, "utf8"))


def main():
    """
    main - Main function
    Return: Void
    """
    with HTTPServer(("", 8000), ServerHandler) as httpd:
        httpd.serve_forever()


if __name__ == "__main__":
    main()
