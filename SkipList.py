class SkipListNode:
    def __init__(self, lower, next):
        self.lower = None
        self.upper = None
        self.next = None
        self.linkwidth = 0 # LinkWidth will be later implemented for O(log n) index lookup.

# Supports search, insert, and delete on (num, value) key-value pairs
# Can be initialized via array of these tuples.
class SkipList:
    def __init__(self, kvs): 