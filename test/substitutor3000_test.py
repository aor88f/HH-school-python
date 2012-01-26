import unittest
import substitutor3000


class TestSubstitutor3000(unittest.TestCase):
    def testReplace1(self):
        sbst = substitutor3000.Substitutor3000();
        sbst.put("k1", "one");
        sbst.put("k2", "two");
        sbst.put("keys", "1: ${k1}, 2: ${k2}");        
        self.assertEqual("1: one, 2: two", sbst.get("keys"));

    def testReplace2(self):
        sbst = substitutor3000.Substitutor3000();
        sbst.put("X", "ONE");
        sbst.put("Y", "TWO");
        sbst.put("abcTWOdef", "THREE");
        sbst.put("keys", "1: ${X}, 3: ${abc${Y}def}");        
        self.assertEqual("1: ONE, 3: THREE", sbst.get("keys"));


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
