import re

class Substitutor3000:
    map = dict()
    reVar = '\$\{[^\$]*?\}'
    p = re.compile(reVar)
    
    def put(self, key, value):
        map[key] = value
        
    def get(self, key):
        value = key.get(key)
        return ("") if (value == None) else (self.replace(value))
    
    def replace(self, s):
        sub = self.p.sub('#', s)
        return (sub) if (sub == s) else (self.replace(sub))
