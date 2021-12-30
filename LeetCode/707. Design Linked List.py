class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.arr = []

    def print(self):
        val = []
        for i in self.arr:
            val.append(i.val)
        print(val)

    def get(self, index: int) -> int:
        if 0 <= index < len(self.arr):
            return self.arr[index].val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        new = ListNode(val)
        if self.arr:
            new.next = self.arr[0]
        self.arr.insert(0, new)
        return self.arr[0]

    def addAtTail(self, val: int) -> None:
        new = ListNode(val)
        if self.arr:
            self.arr[-1].next = new
        self.arr.append(new)
        return self.arr[0]

    def addAtIndex(self, index: int, val: int) -> None:
        if not self.arr:
            if index == 0 or index == -1:
                new = ListNode(val)
                self.arr.append(new)
                return self.arr[0]
            else:
                return
        else:
            if index == 0:
                self.addAtHead(val)
            elif index > len(self.arr):
                return self.arr[0]
            elif index == len(self.arr):
                self.addAtTail(val)
            else:
                new = ListNode(val)
                pre = self.arr[index - 1]
                pre.next, new.next = new, self.arr[index]
                self.arr.insert(index, new)
                return self.arr[0]

    def deleteAtIndex(self, index: int) -> None:
        if 0 < index < len(self.arr):
            if index != len(self.arr) - 1:
                self.arr[index - 1].next = self.arr[index + 1]
            else:
                self.arr[index - 1].next = None
            del self.arr[index]
            return self.arr[0]
        elif index == 0:
            self.arr.pop(0)
            if self.arr:
                return self.arr[0]
            else:
                return
        else:
            if self.arr:
                return self.arr[0]
            else:
                return
