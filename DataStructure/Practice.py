class HashTable:
    def __init__(self):
         self.table = [[] for i in range(20)] 
    def hash_it(self, var):
        hashed_value = 0
        for i in var:
            hashed_value += ord(i)
        store = hashed_value % 100
        return store
 
    def __setitem__(self, key, value):
       
        self.this_position = self.hash_it(key)
        self.table[self.this_position].append((key, value))
            

obj = HashTable()
obj['march 6'] = 69
print(obj.table)     


