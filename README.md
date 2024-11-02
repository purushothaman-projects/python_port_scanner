Here’s a complete documentation of the provided port scanner code, outlining its purpose, functionality, and usage:

---

# Port Scanner Documentation

## Overview

This port scanner is a Python script designed to identify open ports on a specified IP address. By establishing socket connections to the target IP for a range of ports, the scanner can determine which ports are accessible and open for communication. This can be useful for network diagnostics and security assessments.

## Features

- Validates IP addresses to ensure they are in the correct format.
- Allows users to specify a range of ports to scan.
- Reports open ports found during the scan.
- Handles potential connection errors gracefully.
- Displays a user-friendly output for ease of understanding.

## Requirements

To run this script, you need:

- Python 3.x installed on your machine.
- Basic knowledge of how to run Python scripts in your environment.

## Code Structure

### 1. Imports

```python
import socket
import re
```

The script imports the `socket` module for network communication and the `re` module for regular expression operations to validate IP addresses.

### 2. Welcome Message

A decorative welcome message is printed to the console when the script runs, branding it as developed by "SecureShifu."

```python
print("""...""")
```

### 3. IP Address Validation Function

```python
def is_valid_ip(ip):
    """Check if the provided IP address is valid."""
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return re.match(pattern, ip) is not None
```

- **Purpose**: Validates if the entered IP address follows the standard IPv4 format (e.g., `192.168.1.1`).
- **Input**: A string representing the IP address.
- **Output**: Returns `True` if valid, otherwise `False`.

### 4. User Input

The script prompts the user for input:

```python
ip = input('Enter the IP for Scanning: ')
start_ip = int(input('Enter Start Port: '))
end_ip = int(input('Enter End Port: '))
```

- **IP Address**: The target IP to scan.
- **Port Range**: The starting and ending ports for the scan.

### 5. IP Address Validation

Before proceeding with the port scan, the script checks if the entered IP address is valid:

```python
if not is_valid_ip(ip):
    print("Oops! That doesn't seem to be a valid IP address. Please check and try again.")
```

### 6. Port Scanning Function

```python
def scanPort(target_ip):
    """Scan ports on the given target IP address."""
    ...
```

- **Purpose**: Scans the specified range of ports on the target IP address.
- **Parameters**: 
  - `target_ip`: The IP address to scan.
  
### 7. Loop Through Ports

Inside the `scanPort` function, the script uses a loop to check each port in the specified range:

```python
for port in range(start_ip, end_ip):
```

- **Socket Creation**: For each port, a socket is created to attempt a connection.
- **Timeout**: A timeout of 0.5 seconds is set to avoid long waits.

### 8. Connection Attempt

```python
result = sock.connect_ex((target_ip, port))
```

- **Success Check**: If `result` equals `0`, the port is open, and it’s recorded:

```python
if result == 0:
    print(f'Found open port: {port}')
```

### 9. Error Handling

The script handles any connection errors gracefully:

```python
except socket.error as e:
    print(f'Error connecting to port {port}: {e}')
```

### 10. Socket Closure

Each socket is closed after its use to free resources:

```python
finally:
    sock.close()
```

### 11. Displaying Results

At the end of the scan, the script displays the results:

```python
if open_ports:
    print(f'Result: Open ports found: {open_ports}')
else:
    print('No open ports found.')
```

## Running the Script

1. Copy the script into a Python file (e.g., `port_scanner.py`).
2. Open your command line or terminal.
3. Navigate to the directory where the script is located.
4. Run the script using Python:

   ```bash
   python port_scanner.py
   ```

5. Follow the prompts to enter the target IP address and port range.

## Conclusion

This port scanner serves as a basic tool for network exploration and can help identify open ports on a given IP address. It can be further enhanced by adding features such as multi-threading for faster scanning or implementing more robust error handling and reporting.

---

This documentation should provide a clear understanding of your port scanner's functionality, structure, and how to use it effectively.

Thank you for reading, see you 
SecureShifu 
