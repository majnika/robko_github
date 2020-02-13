import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

addr = ("0.0.0.0", 12345)

sock.bind(addr)

sock.recv(1518)

sock.close()