import socket


class TCPServer:
    def __init__(self, host='127.0.0.1', port=65432):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM).__enter__()
        self.socket.bind((host, port))
        self.socket.listen()
        self.connection, self.address = self.socket.accept()

    def __del__(self):
        self.socket.__exit__()

    def receive(self, size=1024):
        return self.connection.recv(size)

    def send(self, payload):
        self.connection.sendall(payload)

