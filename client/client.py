from socket import *
from typing import *

host = gethostname()
port = 55551

client = socket(AF_INET, SOCK_STREAM)
client.connect((host, port))

while True:
    msg = input("Digite: ")
    client.send(msg.encode())
