import socket
def main():
    HostName = socket.gethostbyname()
    ipaddr = socket.gethostbyname(HostName)
    print ("Host Name is:{}".format(HostName))
    print ("IpAdrr is :{}".format(ipaddr))
