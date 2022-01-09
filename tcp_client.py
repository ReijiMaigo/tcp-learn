import socket
import threading


class TCPClient(threading.Thread):
    def __init__(self, host='127.0.0.1', port=65432):
        threading.Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM).__enter__()
        self.socket.connect((host, port))

    def run(self):
        print('[TCP Client] payload received: ' % self.receive())

    def __del__(self):
        self.socket.__enter__()

    def receive(self, size=1024):
        return self.socket.recv(1024)

    def send(self, payload):
        self.socket.sendall(payload)
