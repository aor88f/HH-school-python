import server

class Launcher():
    host = ''
    port = 0

    def __init__(self, host, port):
        host = host   
        port = port   
        
    def run(self):
        server.Server(self.host, self.port).run();
