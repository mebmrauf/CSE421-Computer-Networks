import socket
import threading

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

def serveAClient(clientSocket, clientAddress):
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
                vowel = "aeiouAEIOU"
                count = 0
                for char in message:
                    if char in vowel:
                        count += 1
                    if count > 2:
                        break
                if count == 0:
                    clientSocket.send("Not enough vowels".encode(format))
                elif count <= 2:
                    clientSocket.send("Enough vowels I guess".encode(format))
                else:
                    clientSocket.send("Too many vowels".encode(format))
                print("\n")
    clientSocket.close()

while True: # multi-threaeding
    clientSocket, clientAddress = server.accept()
    thread = threading.Thread(target=serveAClient, args = (clientSocket, clientAddress))
    thread.start()