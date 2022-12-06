import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 54321))
    s.listen()
    connection, _address = s.accept()
    with connection:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            connection.sendall(data)
