import socket

serverPort = 8080
format = 'utf-8'
bufferForMessageLength = 16

# create the server's address - socket
hostName = socket.gethostname()
hostIP = socket.gethostbyname(hostName)
serverAddress = (hostIP, serverPort)

# create the server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the server socket to the address
server.bind(serverAddress)
server.listen()
print(f"Server is listening on {hostIP}:{serverPort}")
while True:
    # accept connections from clients
    clientSocket, clientAddress = server.accept()
    print(f"Connection established with {clientAddress}")

    connected = True
    while connected:
        # receive the length of the incoming message
        messageLength = int(clientSocket.recv(bufferForMessageLength).decode(format))
        print(f"Upcoming message length: {messageLength}")

        if messageLength:
            message = clientSocket.recv(messageLength).decode(format)

            if message == "Disconnect":
                connected = False
                print(f"Terminating connection with {clientAddress}")
                clientSocket.send("The session is terminated".encode(format))
                print("\n")
            else:
                print(f"Received message: {message}")
                clientSocket.send("The server has received the message received".encode(format))
                print("\n")
    clientSocket.close()