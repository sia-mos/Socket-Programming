import socket

HOST = "127.0.0.1"
PORT = 65432

client = socket.socket()
client.connect((HOST, PORT))

while True:
    command = input("Enter command: ")

    if command == "LIST":
        client.send(command.encode())
        print(client.recv(4096).decode())

    elif command.startswith("DOWNLOAD"):
        client.send(command.encode())

        response = client.recv(1024)

        if response == b"OK":
            client.send(b"READY")
            filename = command.split()[1]

            data = client.recv(4096)

            with open("downloaded_" + filename, "wb") as file:
                file.write(data)

            print("Download complete")
        else:
            print("File not found")

    elif command.startswith("UPLOAD"):
        filename = command.split()[1]

        with open(filename, "rb") as file:
            data = file.read()

        command = "UPLOAD " + filename + " " + str(len(data))
        client.send(command.encode())

        if client.recv(1024) == b"READY":
            client.sendall(data)
            print(client.recv(1024).decode())

    elif command == "EXIT":
        client.send(command.encode())
        break

client.close()
