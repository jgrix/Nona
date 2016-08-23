import SocketServer
import threading
import thread
import atexit
from time import sleep

data = ""
lock = threading.Lock()

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
        The request handler class for our server.
        
        It is instantiated once per connection to the server, and must
        override the handle() method to implement communication to the
        client.
        """
    
    def handle(self):
        # self.request is the TCP socket connected to the client
        global data
        global lock
        try:
            lock.acquire()
            data = self.request.recv(1024).strip()
            data2 = data
            print "{} wrote:".format(self.client_address[0])
            print data
            # just send back the same data, but upper-cased
            self.request.sendall(data.upper())
            print("end of handle")
        finally:
            lock.release()

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


class Andriod_Comms(MyTCPHandler):
    
    HOST = "localhost"
    PORT = 9999
    server = ThreadedTCPServer((HOST, PORT), MyTCPHandler)
    
    def myExit(self):
        self.server.shutdown()
        self.server.server_close()

    def __init__(self, cb1):
        self.cb1 = cb1
        atexit.register(self.myExit)
	print("TCP back end started!")
    
    def start(self):
        thread.start_new_thread(self.start_Comms, ())

    def start_Comms(self):
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()
        self.monitor_Loop()

    def monitor_Loop(self):
        global data
        global lock
        while True:
            try:
                lock.acquire()
                if data:
                    self.cb1(data)
                    data = ""
            finally:
                lock.release()
                sleep(1)




if __name__ == "__main__":
    
    global data
    def callback(arg1):
        print(arg1)

    myComm = Andriod_Comms(callback)
    myComm.start()

    while True:
        sleep(5)


