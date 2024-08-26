import socket
import threading
from time import sleep


def recieveing():
    while True:
        global data_in
        data_chunk = ya_socket.recv(1024)
        data_in = data_in + data_chunk

ya_socket = socket.socket()
ya_socket.connect(('77.88.55.242', 443))
data_out = b"GET / HTTP/1.1\r\nHost:ya.ru\r\n\r\n"

ya_socket.send(data_out)
data_in = b""
rec_thread = threading.Thread(target=recieveing)
rec_thread.start()

sleep(4)

print(data_in)

ya_socket.close()