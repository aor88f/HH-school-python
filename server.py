import asyncore
import socket
import time
import substitutor3000

_sbst = substitutor3000.Substitutor3000()

class Handler(asyncore.dispatcher_with_send):
    sleep = 0
    
    def handle_read(self):
        
        data = self.recv(8192).rstrip()
        time.sleep(self.sleep)
        if data:
            com, param = self._sep(data)
            param, param2 = self._sep(param)
            if com == 'GET':
                self.send('VALUE\n')
                self.send(_sbst.get(param) + '\n')
            elif com == 'PUT':
                self.send('OK\n')
                _sbst.put(param, param2)
            elif com == 'SET':
                if param == 'SLEEP':
                    self.send('OK\n')
                    try:
                        self.sleep = int(param2) / 1000.0
                        if self.sleep < 0:
                            raise Exception()
                    except Exception:
                        self.sleep = 0
                    
            
        self.close()

    def _sep(self, s):
        i = s.find(' ')
        return (s, '') if (i == -1) else (s[:i], s[i+1:])


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

