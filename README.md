# Socket-Programming-Homework
A simple TCP client-server file transfer system implemented using Python socket programming.



# Custom FTP Server using Socket Programming (Python)

A simple **client-server file transfer application** developed in Python using **socket programming**.
The project demonstrates how a client and server communicate over a network to perform basic file transfer operations.

## Project Structure

* `server.py` – Runs the FTP server and handles client connections and file operations.
* `client.py` – Connects to the server and provides commands for file transfer.
* `README.md` – Contains project information and execution instructions.

## Key Features

* **LIST** – Displays the files available on the server.
* **UPLOAD** – Uploads a file from the client to the server.
* **DOWNLOAD** – Downloads a file from the server to the client.
* **EXIT** – Disconnects the client safely from the server.

## Technologies Used

* **Python**
* **Socket Programming**
* **TCP/IP Communication**

## How to Run

### Step 1: Open the Project

Open the project folder in **VS Code**.

### Step 2: Start the Server

Open a terminal and run:

```bash
python server.py
```

Keep the server terminal running.

### Step 3: Start the Client

Open another terminal in the same project folder and run:

```bash
python client.py
```

### Step 4: Use the Commands

After connecting to the server, use the available commands:

```text
LIST
UPLOAD
DOWNLOAD
EXIT
```

## Example

The server waits for a client connection:

```text
Server started...
Waiting for connection...
```

The client connects to the server and can then perform file operations such as listing, uploading, and downloading files.

## Learning Outcome

This project provides practical experience with:

* Client-server architecture
* TCP socket communication
* File handling in Python
* Data transfer between client and server
* Basic network programming

## Author

**Md. Siam Osman**

