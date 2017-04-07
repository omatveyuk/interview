""" Hash table implementation
    >>> ht = HashTable()
    >>> ht.set('a', 1)
    >>> ht.set('aa', 2)
    >>> ht.set('aaa', 3)
    >>> ht.display()
    { 'aaa' : 3 , 'a' : 1 , 'aa' : 2 , }
    >>> ht.get('aaa')
    3
    >>> ht.delete('aa')
    >>> ht.display()
    { 'aaa' : 3 , 'a' : 1 , }

    >>> ht = HashTable()
    >>> ht.set('b', 98)
    >>> ht.set('bb', 196)
    >>> ht.set('bbb', 294)
    >>> ht.set('abc', 294)
    >>> ht.display()
    { 'bbb' : 294 , 'abc' : 294 , 'b' : 98 , 'bb' : 196 , }
    >>> ht.get('bbb')
    294
    >>> ht.get('abc')
    294
    >>> ht.delete('bbb')
    >>> ht.display()
    { 'abc' : 294 , 'b' : 98 , 'bb' : 196 , }

"""
class KeyValue(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable(object):
    SIZE = 256
    def __init__(self):
        # implement hash table as list of lists to solve problem with colision
        # Our internal list is a list of buckets, where each bucket
        # holds all the key, value pairs that map to a particular index
        self.hashlst = [[] for i in xrange(self.SIZE)]

    def set(self, key, value):
        """Put pair key, value in Hash Table with index from hash(key)"""
        index_hashlst = self._hash(key)
        self.hashlst[index_hashlst].append(KeyValue(key, value))

    def get(self, key):
        """Get pair value from Hash Table by hash(key)"""
        index_hashlst = self._hash(key)
        for item in self.hashlst[index_hashlst]:
            if item.key == key:
                return item.value

    def delete(self, key):
        """Delete pair ket, value from Hash Table with index from hash(key)"""
        index_hashlst = self._hash(key)
        for item in self.hashlst[index_hashlst]:
            if item.key == key:
                self.hashlst[index_hashlst].remove(item)

    def _hash(self, key):
        """ Calculate index in Hash Table """
        total = sum([ord(char) for char in key])
        return total % self.SIZE

    def display(self):
        print "{",
        for item in self.hashlst:
            for each in item:
                print "'"+each.key+"'",":",each.value,",",
        print "}"

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!!!! ***\n"

