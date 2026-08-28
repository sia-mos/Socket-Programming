import socket
import os

HOST = "127.0.0.1"
PORT = 65432

server = socket.socket()
server.bind((HOST, PORT))
server.listen(1)

print("Server started...")
conn, addr = server.accept()
print("Client connected")

while True:
    command = conn.recv(1024).decode()

    if command == "LIST":
        files = os.listdir(".")
        conn.send("\n".join(files).encode())

    elif command.startswith("DOWNLOAD"):
        filename = command.split()[1]

        if os.path.isfile(filename):
            conn.send(b"OK")
            conn.recv(1024)

            with open(filename, "rb") as file:
                data = file.read()
                conn.sendall(data)
        else:
            conn.send(b"ERROR")

    elif command.startswith("UPLOAD"):
        parts = command.split()
        filename = parts[1]
        size = int(parts[2])

        conn.send(b"READY")

        data = b""
        while len(data) < size:
            data += conn.recv(4096)

        with open("uploaded_" + filename, "wb") as file:
            file.write(data)

        conn.send(b"SUCCESS")

    elif command == "EXIT":
        break


conn.close()
server.close()
