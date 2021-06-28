import socket
from binascii import hexlify
def ipconversion():
    for ip_addr in ["127.0.0.1", "192.168.0.1"]:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print("ip address:{} => packed :{} , unpacked:{}".format(ip_addr, hexlify(packed_ip_addr)))

ipconversion()