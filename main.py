import threading

from tcp_server import TCPServer
from tcp_client import TCPClient


def start_tcp_server():
    tcp_server = TCPServer()
    payload = tcp_server.receive()
    print('[Server]: payload received: %s.' % payload.decode())
    tcp_server.send(b'good')


def main():
    t1 = threading.Thread(target=start_tcp_server)
    t1.start()
    tcp_client = TCPClient()
    tcp_client.start()
    tcp_client.send((b'asdf'))



if __name__ == '__main__':
    main()
