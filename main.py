
# Dark Net
# Created By Swev#9999
# POC DDoS Net

import socket
import requests

server_address = "1.1.1.1" # CHANGE THIS
port = 9999 # CHANGE THIS IF YOU KNOW WHAT YOU'RE DOING

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((server_address, port))

def handle(client):
  try:
    client.send("Welcome To Dark".encode())
   except:
    pass # connection closed
