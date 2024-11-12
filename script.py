import socket

ip = input("IP address to scan: ")

# Loop thorugh the 65535 exsisting ports.
for port in range(1, 65535):

    # Create a socket (socket.AF_INET to use IPv4.), (socket.SOCK_STREAM to use TCP protocol)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    result = sock.connect_ex((ip, port))

    # 0 = open port
    if result == 0:
        print("Open port: " + str(port))
    else:
        print("Closed port: " + str(port))
