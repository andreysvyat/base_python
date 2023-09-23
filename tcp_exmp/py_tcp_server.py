import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 12345))
sock.listen(5)
i = 0
while True:
    connection, address = sock.accept()
    buf = connection.recv(1024)
    try:
        print(buf.decode('utf-8'))
    except UnicodeDecodeError:
        print()
        print(buf)
        print()
    connection.send(b'HTTP/1.1 200 OK\r\n'
                    b'Server:python\r\n\r\n'
                    b'response ' + str(i).encode('utf-8'))
    i += 1
    connection.close()
