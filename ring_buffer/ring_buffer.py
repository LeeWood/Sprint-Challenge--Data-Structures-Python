class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        oldest = self.storage[0]
        #we need to id the oldest item and replace it when the ring is full.

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage.pop(0) #removes from front
        self.storage.append(item) #adds to end

    def get(self):
        return self.storage