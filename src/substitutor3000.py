import re

class Substitutor3000:
    _mp = dict()
    _reVar = '\$\{[^\$]*?\}'
    _p = re.compile(_reVar)

    def put(self, key, value):
        self._mp[key] = value

    def get(self, key):
        value = self._mp.get(key)
        return self._replace(value) if value else ''

    def _replace(self, s):
        m = self._p.search(s)
        if m:
            g = m.group(0)
            x = g[2:-1]
            r = self._mp.get(x)
            if r is None:
                r = ''
            s2 = s.replace(g, r)
            if s != s2:
                s = self._replace(s2)
        return s
