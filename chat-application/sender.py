import socket
import select
import errno
import sys
import time
from threading import Timer
import os

HEADER_LENGTH = 3

print("Sender Client")
IP = input("Enter IP: ") #"192.168.1.117"
PORT = int(input("Enter PORT: ")) #9876

message = None
my_username = input("Username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP,PORT))
client_socket.setblocking(False)

username = my_username.encode("utf-8")
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
client_socket.send(username_header + username)
print('Sent Username')

def send_msg(msg):
    message = msg.encode("utf-8")
    message_header = f"{len(message):<{HEADER_LENGTH}}".encode("utf-8")
    #message_list.append(message)

    client_socket.send(message_header + message)


def nextStep():
    message = input(f"{my_username}: ")
    send_msg(message)
    nextStep()

nextStep()
