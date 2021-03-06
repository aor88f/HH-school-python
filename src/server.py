import asyncore
import socket
import time
import substitutor3000


class Handler(asyncore.dispatcher_with_send):
    _sbst = substitutor3000.Substitutor3000()
    _sleep = 0

    def handle_read(self):
        data = self.recv(8192).rstrip()
        time.sleep(self._sleep)
        if data:
            com, param = self._sep(data)
            param, param2 = self._sep(param)
            if com == 'GET':
                self.send('VALUE\n' + self._sbst.get(param) + '\n')
            elif com == 'PUT':
                self._sbst.put(param, param2)
                self.send('OK\n')
            elif com == 'SET':
                if param == 'SLEEP':
                    try:
                        self._sleep = int(param2) / 1000.0
                        if self._sleep < 0:
                            raise Exception()
                    except Exception:
                        self.close()
                    self.send('OK\n')
        self.close()

    def _sep(self, s):
        i = s.find(' ')
        return (s, '') if (i == -1) else (s[:i], s[i+1:])


class Server(object, asyncore.dispatcher):
    
    def __init__(self, host, port):
        object.__init__(self)
        self._port = port
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

if __name__ == "__main__":
    server = Server('', 12322)
    server.run()
