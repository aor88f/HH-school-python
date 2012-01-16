import server

class Launcher():
    _host = ''
    _port = 0

    def __init__(self, host, port):
        _host = host   
        _port = port   
        
    def run(self):
        server.Server(self._host, self._port).run();
