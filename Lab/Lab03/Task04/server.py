import socket

serverPort = 8080
format = 'utf-8'
bufferForMessageLength = 16

hostName = socket.gethostname()
hostIP = socket.gethostbyname(hostName)
serverAddress = (hostIP, serverPort)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(serverAddress)
server.listen()
print(f"Server is listening on {serverAddress}")

while True:
    clientSocket, clientAddress = server.accept()
    print(f"Connection established with {clientAddress}")

    connected = True
    while connected:
        messageLength = clientSocket.recv(bufferForMessageLength).decode(format)
        print(f"Upcoming message length: {messageLength}")

        if messageLength:
            messageLength = int(messageLength.strip())
            message = clientSocket.recv(messageLength).decode(format)

            if message == "Disconnect":
                connected = False
                print(f"Terminating connection with {clientAddress}")
                clientSocket.send("The session is terminated".encode(format))
                print("\n")
            else:
                print(f"Received message: {message}")
                if message.replace('.', '', 1).isdigit():
                    hours = int(message)
                    if hours <= 40:
                        salary = hours * 200
                    else:
                        salary = 8000 + 300 * (hours - 40)
                    reply = f"Salary: Tk {salary}"
                else:
                    reply = "Invalid input."
                clientSocket.send(reply.encode(format))
                print("\n")
    clientSocket.close()