import server

class Launcher(object):
    
    def __init__(self, host, port):
        self._host = host
        self._port = port

    def run(self):
        server.Server(self._host, self._port).run();

Launcher('', 12322).run()
