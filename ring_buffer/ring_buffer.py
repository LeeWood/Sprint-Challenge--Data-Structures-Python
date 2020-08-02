class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        #oldest index to be used when deleting and replacing oldest item in self.storage
        self.oldestIndex = 0 
        
    def setOldest(self):
        self.oldestIndex = (self.oldestIndex + 1) % self.capacity
        #keeping oldest index from incrementing past capacity

    def append(self, item):
        #if adding to list that's not full...
        if len(self.storage) <= self.capacity - 1:
            self.storage.append(item)
        else:
            self.storage[self.oldestIndex] = item
        self.setOldest()

    def get(self):
        return self.storage