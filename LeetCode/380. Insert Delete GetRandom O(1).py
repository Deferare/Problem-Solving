class RandomizedSet:
    def __init__(self):
        self.set_my = set()

    def insert(self, val: int) -> bool:
        if val not in self.set_my:
            self.set_my.add(val)
            return True
        else:
            return False
    def remove(self, val: int) -> bool:
        if val in self.set_my:
            self.set_my.remove(val)
            return True
        else:
            return False
    def getRandom(self) -> int:
        arr = [value for value in self.set_my]
        return arr[random.randint(0,len(arr)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
