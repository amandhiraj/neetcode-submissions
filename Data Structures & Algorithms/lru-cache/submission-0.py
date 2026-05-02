class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            # This line moves the key to the end to show that it was recently used
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Move the key to the end to show that it was recently used
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # Remove the first key (least recently used)
            self.cache.popitem(last=False)
        # Insert the item
        self.cache[key] = value