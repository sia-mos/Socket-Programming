# Custom FTP Server using Python Sockets

## Overview

This project is a simple client-server file transfer system created using Python's
socket programming. It demonstrates how two programs can communicate over a
network and exchange files using TCP connections.

The server manages the files, while the client sends requests to perform
different file operations.

## How It Works

The project consists of two main programs:

- **Server** – Waits for a client connection and handles file-related requests.
- **Client** – Connects to the server and allows the user to interact with it.

The communication takes place through a TCP socket connection.

## Available Operations

The client can request the server to:

| Command | Purpose |
|---------|---------|
| `LIST` | View the files available on the server |
| `UPLOAD` | Send a file from the client to the server |
| `DOWNLOAD` | Receive a file from the server |
| `EXIT` | Close the connection |

## Project Files

```text
Custom-FTP-Server/
│
├── server.py
├── client.py
└── README.md
server.py

Contains the server-side code. It creates the socket, waits for a client,
receives requests, and performs the required file operations.

client.py

Contains the client-side code. It connects to the server and sends commands
for listing, uploading, and downloading files.

Requirements
Python 3.x
Basic knowledge of Python
A computer with VS Code or another Python IDE

No external Python libraries are required.

Running the Project
1. Start the Server

Open a terminal in the project directory and run:

python server.py

The server will start and wait for a client connection.

2. Start the Client

Open a second terminal in the same project directory and run:

python client.py

The client will connect to the running server.

3. Perform File Operations

After connecting, use the available commands to list, upload, download,
or exit the application.

Technologies
Python 3
Socket Programming
TCP/IP
Client-Server Architecture
File Handling
Learning Objectives

This project helps demonstrate:

How TCP socket communication works
How a client and server communicate
Basic network programming in Python
Sending and receiving data through sockets
File transfer between two programs
Conclusion

The project provides a basic implementation of a custom FTP-style file
transfer system using Python sockets. It demonstrates the fundamental
concepts of client-server communication and network-based file sharing.

