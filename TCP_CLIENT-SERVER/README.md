This project demonstrates the basic implementation of a TCP (Transmission Control Protocol) Client-Server model** using Python's built-in `socket` module. It illustrates how a client and a server establish a connection and exchange messages over a network.

## Features

* Establishes a TCP connection between a client and a server.
* Server listens for incoming client connections.
* Client connects to the server using the server's IP address and port number.
* Supports basic message exchange between the client and the server.
* Demonstrates reliable communication using the TCP protocol.

---

## Technologies Used

* Python 3
* Socket Programming (`socket` module)
* TCP/IP Protocol

---

## Project Structure

.
├── server.py      # Starts the TCP server
├── client.py      # Connects to the server and sends messages
└── README.md
```
How It Works

##Server

1. Creates a TCP socket.
2. Binds the socket to a host and port.
3. Starts listening for incoming client connections.
4. Accepts a client connection.
5. Receives data sent by the client.
6. Sends a response back to the client.
7. Closes the connection after communication is complete.

##Client

1. Creates a TCP socket.
2. Connects to the server using the server's IP address and port number.
3. Sends a message to the server.
4. Receives the server's response.
5. Closes the connection.



## Future Improvements

* Support multiple clients simultaneously using multithreading.
* Implement continuous two-way communication.
* Add error handling and connection timeout mechanisms.
* Create a simple graphical interface (GUI).
* Encrypt messages for secure communication.

---

#AUTHOR

KRATIKA SRIVASTAVA

This project was created as part of my learning journey in **Python Networking and Socket Programming** and will add more features like multi-threading and encryption.

