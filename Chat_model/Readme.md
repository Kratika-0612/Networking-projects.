# Multi-Client TCP Chat Application

A multi-client TCP Chat Application developed in Python using the `socket` and `threading` modules. The application enables multiple clients to establish concurrent TCP connections with a server, allowing independent communication sessions without interrupting other connected clients.

The project demonstrates the implementation of socket programming, multithreading, and concurrent client handling in a client-server architecture.

---

## Features

* Multi-client communication over TCP
* Concurrent client handling using multithreading
* Dedicated thread for every connected client
* Continuous message exchange until the connection is terminated
* Graceful handling of client disconnections
* Server remains active even when individual clients disconnect
* Exception handling for reliable execution
* Modular and readable code structure

---

## Technologies Used

* Python 3
* Socket Programming
* TCP/IP Networking
* Multithreading (`threading` module)

---

## Project Architecture

                    Server
                      │
               Create TCP Socket
                      │
              Bind Host and Port
                      │
                  Start Listening
                      │
              Accept New Client
                      │
          Create a New Thread
                      │
                      ▼
             handle_client()
                      │
      Receive Message ↔ Send Reply
                      │
          Continue Until Disconnect
                      │
             Close Client Socket


---

## Project Structure

```
server.py
client.py
```

### Server Responsibilities

* Create a TCP socket.
* Bind the socket to the specified host and port.
* Listen for incoming client connections.
* Accept client connections continuously.
* Create a dedicated thread for each connected client.
* Handle communication independently for every client.

### Client Responsibilities

* Create a TCP socket.
* Connect to the server.
* Send messages to the server.
* Receive server responses.
* Continue communication until the user exits or the server disconnects.

---

## How It Works

1. The server creates a TCP socket and starts listening for incoming connections.
2. When a client connects, the server accepts the connection.
3. A separate thread is created to handle communication with that client.
4. Multiple clients can communicate with the server simultaneously.
5. Each client exchanges messages independently.
6. If a client disconnects, only its thread terminates while the server continues serving other clients.


---

## Learning Outcomes

Through this project, I gained practical experience with:

* TCP socket programming
* Multi-client server architecture
* Concurrent client handling using threads
* Designing modular networking applications
* Managing socket connections safely
* Implementing graceful exception handling
* Understanding real-time client-server communication

---

## Built by-:
Kratika Srivastava :)
