import unittest
import threading
import server

class BaseFunctionalTest(unittest.TestCase, threading.Thread):
    _lock = threading.Lock()
    _server = None

    def __init__(self, x):
        unittest.TestCase.__init__(self, x)
        threading.Thread.__init__(self)

    def __del__(self):
        self._lock.release()

    def port(self):
        return self._server.port()

    def run(self):
        _server = server.Server('', 4324)
        _server.run()
