import unittest
import serverbg


class PutGetTest(unittest.TestCase):
    _serverbg = None

    def __init__(self, methodName='runTest'):
        unittest.TestCase.__init__(self, methodName)
        self._serverbg = serverbg.ServerBg()
        self._serverbg.start()

    def testPutGet(self):
        import socket
        host = 'localhost'
        port = self._serverbg.port()
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send("PUT K1 one")
        self.assertEqual("OK\n", recv(s))
        s.close()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send("GET key")
        self.assertEqual("VALUE\n", recv(s))
        self.assertEqual("one\n", recv(s))  #WTF?
        s.close()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send("PUT keys ${K1} ${K2}")
        self.assertEqual("OK\n", recv(s))
        s.close()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send("GET keys")
        self.assertEqual("VALUE\n", recv(s))
        self.assertEqual("one\n", recv(s))
        s.close()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send("PUT K2 two")
        self.assertEqual("OK\n", recv(s))
        s.close()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send("SET SLEEP 1")
        self.assertEqual("OK\n", recv(s))
        s.close()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send("GET keys")
        self.assertEqual("VALUE\n", recv(s))
        self.assertEqual("one two\n", recv(s))
        s.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

def recv(s):
    return s.recv(8192)
