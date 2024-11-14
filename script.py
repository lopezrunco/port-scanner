import socket
import threading
import re

# Validate IP.
def is_valid_ip(ip):
    regex = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$" # Regex for validating an IPv4 address.
    return re.match(regex, ip)is not None

# Validate port range.
def is_valid_port(port):
    return 1 <= port <= 65535

# Handle & validate IP address input.
def get_ip():
    while True:
        ip = input("IP address to scan: ").strip()
        if is_valid_ip(ip):
            return ip
        else:
            print("Invalid IP address.")

# Handle  & validate port input.
def get_port_range():
    while True:
        try:
            start_port_input = input("Start port (default 1): ").strip()
            end_port_input = input("End port (default: 65535): ").strip()

            # If input is empty, add feault values.
            if not start_port_input:
                start_port = 1
            else:
                start_port = int(start_port_input)

            if not end_port_input:
                end_port = 65535
            else:
                end_port = int(end_port_input) 

            # Validate port range.
            if is_valid_port(start_port) and is_valid_port(end_port) and start_port <= end_port:
                return start_port, end_port
            else:
                print("Invalid port range. Port range must be 1 to 65535.")
        except ValueError:
            print("Invalid input. Please enter valid numeric values for ports.")

# Write the results in a .txt file.
# "a" stands for Append mode: the data will be added to the end of the file rather than overwriting the existing content.
def write_to_file(data):
    with open("results.txt", "a") as f:
        f.write(data + "\n")

def scan_port(port):
    retries = 0

    while retries < max_retries:
        try:
            # Create a socket (socket.AF_INET to use IPv4.), (socket.SOCK_STREAM to use TCP protocol)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))

            # 0 = open port
            if result == 0:
                write_to_file(f"Open port: {port}")
            else:
                write_to_file(f"Closed port: {port}")
            sock.close()
            break # Break if the port is successfully scanned.
        except sock.error:
            retries += 1
            if retries == max_retries:
                write_to_file(f"Failed to scan the port: {port}")
            sock.close()
            break # Break after max entries.

# User input with validation.
ip = get_ip()
start_port, end_port = get_port_range()

timeout = 3
max_retries = 3

# Clear the results file at the start.
with open("results.txt", "w") as f:
    f.write("Port Scan Results\n")
    f.write(f"Scanning IP: {ip}\n")
    f.write(f"Port range: {start_port}-{end_port}\n")
    f.write("=" * 40 + "\n")

# This list will store references to all the created thread objects.
threads = []

# Loop thorugh the specified port range.
for port in range(start_port, end_port + 1):
    # For every port, a thread is created, excecuting the scan_port function in the port.
    thread = threading.Thread(target=scan_port, args=(port,))

    # Add the newly created thread to the threads list.
    threads.append(thread)

    thread.start()

# Iterates over all the started threads. 
# .join ensures the program to wait for each thread to finish its task before continuing.
for thread in threads:
    thread.join()

print("Scan complete. Results saved in results.txt")