import random

MIN_HASH_SIZE = 1

class RandomizedCollection:
    
    def custom_hash(self, val, size):
        return (val + 69) % size
    
    def hash_rebuild(self):
        new_h = [None] * len(self.h) * 2
        self.max_collision_size = 1
        
        for row in self.h:
            if not row:
                continue
            
            for val in row:
                key = self.custom_hash(val, len(new_h))
                if not new_h[key]:
                    new_h[key] = []
                new_h[key].append(val)
                if len(new_h[key]) > self.max_collision_size:
                    self.max_collision_size = len(new_h[key])
        
        self.h = new_h

    def __init__(self):
        self.item_count = 0
        self.max_collision_size = 1
        self.h = [None] * MIN_HASH_SIZE

    def insert(self, val: int) -> bool:
        key = self.custom_hash(val, len(self.h))
        
        ret_val = True
        if self.h[key]:
            if val in self.h[key]:
                ret_val = False
        else:
            self.h[key] = []
        
        self.h[key].append(val)
        if len(self.h[key]) > self.max_collision_size:
            self.max_collision_size = len(self.h[key])
        
        self.item_count += 1
        if self.item_count > len(self.h):
            self.hash_rebuild()
        
        return ret_val

    def remove(self, val: int) -> bool:
        key = self.custom_hash(val, len(self.h))
        
        if not self.h[key] or val not in self.h[key]:
            return False
        
        self.h[key].remove(val)
        self.item_count -= 1
        return True

    def getRandom(self) -> int:
        while True:
            key = random.randint(0, len(self.h) - 1)
            if self.h[key]:
                c = self.h[key]
                c_key = random.randint(0, self.max_collision_size - 1)
                if c_key < len(c):
                    return c[c_key]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
