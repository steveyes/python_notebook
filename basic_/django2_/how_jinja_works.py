import socket
import time


def mock_html():
    return '''<h1 stype="backgroud-color: chartreuse">{{now}}'''


def handle_request(client: socket.socket):
    buf_recvd = client.recv(65535)
    client.send(bytes("HTTP/1.1 200 OK\r\n\r\n", encoding='utf-8'))
    buf_to_send = mock_html()
    client.send(bytes(buf_to_send.replace('{{now}}', str(time.time())), encoding='utf-8'))


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 8888))
    sock.listen(5)

    while True:
        conn, addr = sock.accept()
        handle_request(conn)
        conn.close()


if __name__ == '__main__':
    main()
