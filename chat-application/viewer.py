import socket
import select
import errno
import sys
import time
from threading import Timer
import os

HEADER_LENGTH = 3
MAX_MESSAGES = 20
MESSAGE_TIMEOUT = 1

print("Viewer Client")
IP = input("Enter IP: ") #"192.168.1.117"
PORT = int(input("Enter PORT: ")) #9876

message = None
my_username = "Viewer"#input("Username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP,PORT))
client_socket.setblocking(False)

username = my_username.encode("utf-8")
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
client_socket.send(username_header + username)
print('Sent Username')

message_list = []

def cls():
    # for i in range(1000):
         #print("")
    os.system('cls' if os.name=='nt' else 'clear')

def doNothing():
    #Literally does nothing
    nothing = 0

def send_msg(msg):
    message = msg.encode("utf-8")
    message_header = f"{len(message):<{HEADER_LENGTH}}".encode("utf-8")
    #message_list.append(message)

    client_socket.send(message_header + message)

    time_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", time_tuple)
    message_list.append(f"{time_string} <{my_username}> {msg}")

def receive_msg():
    # try:
    while True:
        username_header = client_socket.recv(HEADER_LENGTH)
        #print(username_header)
        if not len(username_header):
            print("Connection closed by the server")
            sys.exit()
        
        username_length = int(username_header.decode("utf-8").strip())
        username = client_socket.recv(username_length).decode("utf-8")

        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header):
            print("Connection closed by the server")
            sys.exit()
        
        message_length = int(message_header.decode("utf-8").strip())
        message = client_socket.recv(message_length).decode("utf-8")

        time_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%m/%d/%Y, %H:%M:%S", time_tuple)

        print(f"{time_string} <{username}> {message}")

        return f"{time_string} <{username}> {message}"

    # except IOError as e:
    #     if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
    #         print("Reading error", str(e))
    #         sys.exit()

    # except Exception as e:
    #     print("General error", str(e))
    #     sys.exit()

def nextStep():
    cls()
    message_list.sort()
    print("Viewer Client")
    print(f'Connected to {IP}:{PORT}')
    for msg in message_list[-MAX_MESSAGES:]:
        print(msg)

    #print(message_list)

    #message = input(f"{my_username}: ")

    try:
        rec_msg = receive_msg()
        if rec_msg is not None and len(rec_msg) >= 0:
            message_list.append(rec_msg)
    except:
        doNothing()
        #nextStep()
    
    t = Timer(MESSAGE_TIMEOUT, nextStep)
    t.start()
    #message_list.pop()
nextStep()