import socket

# instantiate a socket obj as mysock
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect a socket to site
mysock.connect(('google.com', 80))
# the actual command
cmd = 'GET http://www.google.com HTTP/1.0\n\n'.encode()
# send the cmd to site
mysock.send(cmd)


# loop through data
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

# finally close the connection
mysock.close()