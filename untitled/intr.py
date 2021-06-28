import socket
from socket import AF_INET, SOCK_STREAM
s = socket.socket(family=AF_INET,type= SOCK_STREAM, proto=0)
print("socket created:{}".format(s))