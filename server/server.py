from socket import *

host = gethostname()
port = 55551

print(f'HOST: {host} PORTA {port}')

server = socket(AF_INET, SOCK_STREAM)
server.bind((host, port))
server.listen(5)

while True:
    con, adr = server.accept()
    while 1:
        msg = con.recv(1024)
        print(msg.decode())