import socket
import nmap
from django.shortcuts import render

def scan_ports(ip_address):
    # Create a new nmap PortScanner object
    scanner = nmap.PortScanner()

    # Run a TCP scan on the target IP address
    scanner.scan(ip_address, arguments='-p-')

    # Extract the open ports and their services from the scan result
    open_ports = []
    for port in scanner[ip_address]['tcp']:
        if scanner[ip_address]['tcp'][port]['state'] == 'open':
            service = scanner[ip_address]['tcp'][port]['name']
            open_ports.append((port, service))

    return open_ports

def scanner(request):
    # Check if the user has submitted an IP address
    if 'ip_address' in request.GET:
        # Get the user-provided IP address
        ip_address = request.GET.get('ip_address')

        # Perform a port scan on the IP address
        open_ports = scan_ports(ip_address)

        # Render the results in a template
        context = {'ip_address': ip_address, 'open_ports': open_ports}
        return render(request, 'scanner/results.html', context)

    # Render the scanner form template if no IP address has been submitted yet
    return render(request, 'scanner/scanner.html')
