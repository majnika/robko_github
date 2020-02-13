import socket
from io import StringIO

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_addr = ("127.0.0.1", 12345)

while True:
    message = input("Zadaj spravu: ")

    if message == "END":
        break

    max_data_len = int(input("Zadaj max dlzku dat: "))
    message = message + "&"

    string_file = StringIO(message)
        
    if len(message) > max_data_len:
        while True:
            chunk = string_file.read(max_data_len)
            if len(chunk) > 0:
                sock.sendto(chunk.encode("utf-8"), server_addr)
        
            if  len(chunk) < max_data_len:
                break
    else:
        sock.sendto(message.encode("utf-8"), server_addr)
