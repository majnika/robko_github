import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

addr = ("0.0.0.0", 12345)

sock.bind(addr)

message = []

while True:
    client = sock.recvfrom(1518)
    mesage_bytes = client[0]
    #client_addr = client[1]

    message.append(mesage_bytes.decode("utf-8"))
    
    if mesage_bytes == b'&':
        #print("Hit botka")
        message = message[:-1]
        print("".join(message))
        message = []

sock.close()