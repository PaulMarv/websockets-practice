import socket
import sys
def main():
    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except error as e:
        print("failed to connect")
        print("the failure in connection is as a result of:{}".format(e))
        sys.exit()

    print("socket created successfully")
    targetHost = input("enter the target host:")
    targetPort = input("enter the target port:")

    try:
        s.connect((targetHost, int(targetPort)))
        print("socket " + targetHost)
        print( targetHost + "connected to" + targetPort + "successfully")
        s.shutdown(2)
    except socket.error as e:
        print("failed to connect to" + targetPort)
        print("error occured as a result of",str(e))
        sys.exit()
if __name__ == '__main__':
    main()
