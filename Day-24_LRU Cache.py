"""
Problem statement:
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, 
it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
class LRUCache:

    def __init__(self, capacity: int):
        self.lru = collections.OrderedDict()
        self.capacity = capacity
    def get(self, key: int) -> int:
        if key not in self.lru:
            return -1
        else:
            temp = self.lru.pop(key)    #Assign value to temp and delete it from lru
            self.lru[key] = temp        #Re-add temp to the first position
            return temp
    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.lru.pop(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                self.lru.popitem(last = False)
        self.lru[key]= value

"""
#LeetCode Comments
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
"""
