import socket

def find_ip(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except socket.gaierror:
        return "Error: Couldn't resolve the domain name"

# Example usage:
domain_name = "www.example.com"
ip_address = find_ip(domain_name)
print(f"The IP address of {domain_name} is: {ip_address}")
