class MyHashSet:
    my_set = set()
    def __init__(self):
        self.my_set = set()
    def add(self, key) -> None:
        self.my_set.add(key)
    def remove(self, key) -> None:
        if key in self.my_set:
            self.my_set.remove(key)
    def contains(self, key) -> bool:
        if key in self.my_set:
            return True
        return False
