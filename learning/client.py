
import socket
import pickle

HEADERSIZE = 10

def sendMessage(cs, msg): # Takes socket and message
    message = f'{len(msg):<{HEADERSIZE}}' + msg

        # Send a welcome message. bytes takes the information [1st param] and the type of bytes being sent [2nd param].
    cs.send(bytes(message, "utf-8"))


# create a clientside socket object.
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# connect to the server socket.
s.connect((socket.gethostname(),9876))


while True:

    full_msg = b""
    new_msg = True

    while True:
        # receive a message from the socket. Takes a buffer size (max amt of info to get).
        msg = s.recv(16)

        if(new_msg):
            print(f"Incoming Message of length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg) - HEADERSIZE == msglen :
            rmsg = pickle.loads(full_msg[HEADERSIZE:])

            print(f"Full Message: {rmsg}")

            

            new_msg = True
            full_msg = b""