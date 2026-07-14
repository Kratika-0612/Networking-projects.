ABOUT THE PROJECT-:

A lightweight TCP Single Port Scanner developed in Python using the socket module. The application establishes a TCP connection to a user-specified host and port to determine whether the target port is open or closed. It also identifies the standard application-layer protocol associated with the scanned port using a predefined protocol mapping.

This project was developed as part of my journey in learning Python, Computer Networks, and Cybersecurity.

FEATURES

* Scan a single TCP port on any valid host or domain.
* Determine whether the specified port is OPEN or CLOSED.
* Identify common protocols associated with well-known ports (HTTP, HTTPS, SSH, FTP, DNS, SMTP, etc.).
* Gracefully handle invalid hosts and runtime exceptions.
* Modular and readable code following functional programming principles.

HOW IT WORKS

* The user enters a target host (IP address or domain name).
* The user specifies the port number to scan.
* A TCP socket is created.
* The program attempts to establish a connection using socket.connect_ex().
* The port status is determined based on the connection result.
* The protocol corresponding to the port number is retrieved from the protocol lookup table.
* The scan result is displayed in a structured dictionary format.

TECHNOLOGIES USED

*Python 3
*Socket Programming
*TCP/IP Networking

PROJECT ARCHITECTURE

main()
│

├── Accepts host and port from the user

│

└── scan_port(host, port)
        │
        
        ├── Creates a TCP socket
       
        ├── Attempts a TCP connection
       
        ├── Determines port status
       
        ├── Retrieves protocol information
       
        └── Displays scan results

get_protocol(port)
│

└── Returns the corresponding protocol using a dictionary lookup

LEARNING OUTCOMES

Through this project, I gained practical experience with:

* Python socket programming
* TCP connection workflow
* Network port scanning techniques
* Writing modular and maintainable Python code 
* Implementing robust exception handling
* Designing reusable helper functions

Built By:

KRATIKA SRIVASTAVA :)
