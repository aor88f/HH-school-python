import threading
import server

class ServerBg(threading.Thread):
    _port = 23232

    def __init__(self):
        object.__init__(self)
        threading.Thread.__init__(self)

    def __del__(self):
        pass

    def port(self):
        return self._port

    def run(self):
        server.Server('', self._port).run()


if __name__ == "__main__":
    ServerBg().start()
    print ":)"
