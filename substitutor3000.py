import re

class Substitutor3000:
    mp = dict()
    reVar = '\$\{[^\$]*?\}'
    p = re.compile(reVar)

    def put(self, key, value):
        self.mp[key] = value

    def get(self, key):
        value = self.mp.get(key)
        return self.replace(value) if value else ''

    def replace(self, s):
        m = self.p.search(s)
        if m:
            g = m.group(0)
            x = g[2:-1]
            r = self.mp.get(x)
            if r is None:
                r = ''
            s2 = s.replace(g, r)
            if s != s2:
                s = self.replace(s2)
        return s
