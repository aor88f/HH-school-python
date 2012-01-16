import asyncore
import socket
import substitutor3000

_sbst = substitutor3000.Substitutor3000()

class Handler(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(8192).rstrip()
        if data:
            pass
        self.close()
                

class Server(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is None:
            pass
        else:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            handler = Handler(sock)                      

    def run(self):
        asyncore.loop()

#server = Server('', 12322)
#server.run()
