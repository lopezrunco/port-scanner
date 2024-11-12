# Python Port Scanner

A simple Python-based port scanner that allows you to scan a specified range of ports on a given IP address. The script attempts to connect to each port in the specified range and reports whether the port is open or closed.

## Features:
- [X] **IP Address Validation**: Ensures the provided IP address is a valid IPv4 address.
- [X] **Port Range Validation**: Allows you to specify a range of ports and ensures the range is valid (1 to 65535).
- [X] **Multithreading**: Uses multiple threads to scan ports in parallel, making the scanning process faster.
- [X] **Retries on Failures**: Each port scan is retried up to `max_retries` times if there is a connection failure (e.g., timeouts or unreachable ports).
- [X] **Timeout Configuration**: Supports timeout configuration to limit the time for each port scan attempt.
- [ ] **Thread Pooling** 
- [ ] **Better Output** 
- [ ] **Improved Error Handling** 
- [ ] **Timeout Configuration** 
- [ ] **Support for UDP** 
- [ ] **Progress Bar** 

## Built With:

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Socket](https://img.shields.io/badge/Socket-000000?style=for-the-badge&logo=python&logoColor=white)
![Threading](https://img.shields.io/badge/Threading-000000?style=for-the-badge&logo=python&logoColor=white)
![Regular Expressions](https://img.shields.io/badge/Regex-000000?style=for-the-badge&logo=python&logoColor=white)


## Installation:

Ensure you have Python 3.x installed on your system. You do not need any external libraries for this script to run, as it uses Python's built-in `socket`, `threading`, and `re` modules.

1. Clone this repository or download the script file `port_scanner.py`.

```bash
git clone https://github.com/yourusername/port-scanner.git
cd port-scanner
```

## Usage:

1. Run the script:

Execute the script in your terminal/command prompt:

```sh
python port_scanner.py
```

2. Enter the target IP address:

The script will prompt you to enter the IP address you want to scan. Example:

```sh
IP address to scan: 45.33.32.156
```

3. Enter the port range:

You will then be asked for the start and end ports to scan. If you leave the input blank, the script will default to scanning ports 1-65535:

```sh
Start port (default 1): 
End port (default: 65535): 
```

4. Results:

The script will output whether each port in the range is open or closed:

```sh
Open port: 22
Closed port: 80
Open port: 443
```

#### Example Output:

```sh
IP address to scan: 45.33.32.156
Start port (default 1): 20
End port (default: 65535): 25
Open port: 21
Closed port: 22
Open port: 23
Closed port: 24
Failed to scan port: 25
```

## Disclaimer:

This tool is for educational and personal use only. Scanning ports on networks you do not own or have permission to scan is illegal in many jurisdictions. Always ensure you have proper authorization before using port scanning tools.