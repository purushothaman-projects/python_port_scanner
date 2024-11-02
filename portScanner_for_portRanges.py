import socket
import re
print("""
 888888ba                      dP   .d88888b                                               
 88    `8b                     88   88.    "'                                              
a88aaaa8P' .d8888b. 88d888b. d8888P `Y88888b. .d8888b. 88d888b. 88d888b. .d8888b. 88d888b. 
 88        88'  `88 88'  `88   88         `8b 88'  `88 88'  `88 88'  `88 88ooood8 88'  `88 
 88        88.  .88 88         88   d8'   .8P 88.  .88 88    88 88    88 88.  ... 88       
 dP        `88888P' dP         dP    Y88888P  `88888P8 dP    dP dP    dP `88888P' dP       
+++++++++++++++By SecureShifu | Instagram: secureshifu | Youtube: SecureShifu++++++++++++++                                                                          
                                                                                                                                                                                                                                                                                                                                                                                      
""")

import socket
import re

def is_valid_ip(ip):
    """Check if the provided IP address is valid."""
    # This pattern matches the general format of an IPv4 address (like 192.168.1.1)
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return re.match(pattern, ip) is not None

# Ask the user for the target IP address
ip = input('Enter the IP for Scanning: ')
# Get the starting port number from the user
start_ip = int(input('Enter Start Port: '))
# Get the ending port number from the user
end_ip = int(input('Enter End Port: '))

# Validate the IP address before proceeding
if not is_valid_ip(ip):
    print("Oops! That doesn't seem to be a valid IP address. Please check and try again.")
else:
    def scanPort(target_ip):
        """Scan ports on the given target IP address."""
        print(f'Starting the scan for {target_ip}... Checking ports {start_ip} to {end_ip}.')
        open_ports = []

        # Loop through the specified port range
        for port in range(start_ip, end_ip):  # Scanning the specified port range
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)  # Set a short timeout to avoid waiting too long
            try:
                result = sock.connect_ex((target_ip, port))
                if result == 0:  # If the port is open
                    print(f'Found open port: {port}')
                    open_ports.append(port)  # Add the open port to the list
            except socket.error as e:
                print(f'Error connecting to port {port}: {e}')  # Handle any connection errors
            finally:
                sock.close()  # Always close the socket to free up resources

        # Display the results of the scan
        if open_ports:
            print(f'Result: Open ports found: {open_ports}')
        else:
            print('No open ports found.')

    # Start scanning the ports
    scanPort(ip)
