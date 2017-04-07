"""Create hash table as list of lists

    
"""
class KeyValue(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable(object):
    SIZE = 256
    def __init__(self):
        # implement hash table as list of lists to solve problem with colision
        # We say that our internal list is a list of buckets, where each bucket
        # holds all the key-value pairs that map to a particular index
        self.hashlst = [[] for i in xrange(self.SIZE)]


    def set(self, key, value):
        """Put pair key, value in Hash Table with index from hash(key)"""
        self.index_hashlst = _hash(key)
        self.hashlst[index_hashlst].append((key, value))

    def get(self, key):
        """Get pair key, value from Hash Table by hash(key)"""
        self.index_hashlst = _hash(key)
        for item in self.hashlst[index_hashlst]:
            if item[0] == key:
                return self.hashlst[index_hashlst]

    def _hash(self, key):
        total = sum([ord(char) for char in key])
        return total % self.SIZE

    def display(self):
        print self.hashlst

