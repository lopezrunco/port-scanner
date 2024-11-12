import socket
import threading

ip = input("IP address to scan: ")

def scan_port(port):
    # Create a socket (socket.AF_INET to use IPv4.), (socket.SOCK_STREAM to use TCP protocol)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex((ip, port))

    # 0 = open port
    if result == 0:
        print(f"Open port: {port}")
        sock.close()
    else:
        print(f"Closed port: {port}")

# This list will store references to all the created thread objects.
threads = []

# Loop thorugh the 65535 exsisting ports.
for port in range(1, 65536):
    # For every port, a thread is created, excecuting the scan_port function in the port.
    thread = threading.Thread(target=scan_port, args=(port,))

    # Add the newly created thread to the threads list.
    threads.append(thread)

    thread.start()

# Iterates over all the started threads. 
# .join ensures the program to wait for each thread to finish its task before continuing.
for thread in threads:
    thread.join()