
import socket
import pickle


HEADERSIZE = 10
PORT = 9876

def sendMessage(cs, msg): # Takes socket and message
    msg = pickle.dumps(msg)
    message = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg

        # Send a welcome message. bytes takes the information [1st param] and the type of bytes being sent [2nd param].
    cs.send(message)


# Create a socket object with family type AF_INET/IPV4 [1st param] and type of socket SOCK_STREAM/TCP [2nd param]
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind it to your IP/hostname of the machine [1st param] and a port [2nd param]
s.bind((socket.gethostname(), PORT))

# Start listening on the socket with a queue (max amt of incoming requests) of 5.
s.listen(5)

# Run always
while True:

    # When there's a connection, get the client's socket (they'll have an object for this clientside)
    clientsocket, address = s.accept()

    print(f"Connection from {address} has been established")
    sendMessage(clientsocket, "Welcome to the server!")
