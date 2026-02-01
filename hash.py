class HashSet:
    def __init__(self, initial_capacity=5):
        self.capacity = initial_capacity
        self.size = 0
        self.table = [None] * self.capacity

    def hash(self, key):
        return key % self.capacity

    def quadratic_probe(self, key, i):
        return (self.hash(key) + i**2) % self.capacity

    def add(self, key):
        if self.size / self.capacity >= 0.5:
            self.resize()

        i = 0
        while i <= self.capacity // 2:
            index = self.quadratic_probe(key, i)
            if self.table[index] is None:
                self.table[index] = key
                self.size += 1
                return True
            elif self.table[index] == key:
                return False  # Key already in the set
            i += 1
        
        return False  # Insertion failed after more than half the table was tried

    def resize(self):
        old_table = self.table
        self.capacity *= 2
        self.size = 0
        self.table = [None] * self.capacity
        
        for item in old_table:
            if item is not None:
                self.add(item)

    def display(self):
        for i, v in enumerate(self.table):
            print(f"Index {i}: {v}")

if __name__ == "__main__":
    # Testing the code
    hash_set = HashSet(5)
    values_to_add = [86, 76, 16, 66, 26, 76]

    for value in values_to_add:
        result = hash_set.add(value)
        print(f"Adding {value}: {'Success' if result else 'Failed'}")

    hash_set.display()
