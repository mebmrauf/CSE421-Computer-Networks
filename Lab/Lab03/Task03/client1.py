import socket

serverPort = 8080
format = 'utf-8'
bufferForMessageLength = 16

# create the server's address - socket
hostName = socket.gethostname()
hostIP = socket.gethostbyname(hostName)
serverAddress = (hostIP, serverPort)

# create the client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(serverAddress)
print(f"Connected to server at {serverAddress}")

def sendMessage(message):
    message = message.encode(format)
    # prepare the message length
    messageLength = str(len(message)).encode(format)
    messageLength += b' ' * (bufferForMessageLength - len(messageLength))
    # send the message length and the message
    client.send(messageLength)
    client.send(message)
    # receive the response
    serverMessage = client.recv(2048).decode(format)
    print(f"Server response: {serverMessage}")

while True:
    userInput = input("Enter: ")
    sendMessage(userInput)
    if userInput == "Disconnect":
        break