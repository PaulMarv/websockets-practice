import socket

def main():
    Remote_host = "wwww.slot.ng"

    try:
        print ("ip address of :"+ Remote_host + "is" + socket.gethostbyname(Remote_host))
    except socket.error  as e:
        print("socket error:{}".format(e))
        if _name_ == "_main_":
            main()



