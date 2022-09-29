#!/usr/bin/python

# import BaseHTTPServer, SimpleHTTPServer
from http.server import SimpleHTTPRequestHandler, HTTPServer
import ssl

httpd = HTTPServer(('localhost', 4443), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='./server.pem', server_side=True)
httpd.serve_forever()