import socket
import sys
import select
from datetime import datetime,timedelta


def get_speed(host,port,recvlen):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server and send data
        sock.connect((host, port))
        length=0

        timeout=5
        running = True

        starttime=datetime.now()
        while running :
            data = sock.recv(recvlen)
            if len(data) != 0 :
                length += len(data)
            else :
                break

        timedelta = datetime.now() - starttime
        
        print "Client received %d M data" %  (length/1024/1024)
        print "Speed is %fMbs"% ((length/1024/1024)/timedelta.total_seconds())


    finally:
        sock.close()

if __name__ == "__main__":

    (hostname,port,datalen)=(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))

    
    get_speed(hostname,port,datalen)
