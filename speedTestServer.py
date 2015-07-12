import os
import sys
import struct
import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def __init__(self,datalen=None,times=None):

        self.datalen = datalen if datalen is not None else 1024
        
        self.times = times if times is not None else 1024*1024


    def handle(self):
        bufdata = '1' * self.datalen
        for i in range(self.times):
            self.request.send(bufdata)
            #self.request.sendall('1'*self.datalen)
        print "sent %dM data" % (self.times*self.datalen/1024/1024)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    (host,port,datalen,times) = (sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))

    server = SocketServer.TCPServer((host, port), MyTCPHandler())

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
