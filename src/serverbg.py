import threading
import server

class ServerBg(object, threading.Thread):
    _lock = threading.Lock()
    _port = 23232

    def __init__(self):
        object.__init__(self)
        threading.Thread.__init__(self)

    def __del__(self):
        self._lock.release()
        pass

    def port(self):
        return self._port

    def run(self):
        self._lock.acquire()
        server.Server('', self._port).run()
        self._lock.release()


if __name__ == "__main__":
    ServerBg().start()
    print ":)"
