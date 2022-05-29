#!/usr/bin/env python 
import sys, signal
import socketserver
import http.server


server = socketserver.ThreadingTCPServer(('',8080), http.server.SimpleHTTPRequestHandler )
server.daemon_threads = True   #rende autonomi i thread creati
server.allow_reuse_address = True  #viene usata la stessa porta

try:
  while True:
    print("Server running")
    server.serve_forever()
except KeyboardInterrupt:
  pass

server.server_close()