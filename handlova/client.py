import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_addr = ("127.0.0.1", 12345)

sock.sendto("Hello".encode("utf-8"), server_addr)