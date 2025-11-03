from queue import LifoQueue
class MinStack:

    def __init__(self):
        self.store = LifoQueue()

    def push(self, val: int) -> None:
        if self.store.qsize() > 0:
            first_ele = self.store.queue[-1][1]
            self.store.put((val, min(first_ele, val)))
        else:
            self.store.put((val, val))

    def pop(self) -> None:
        self.store.get()

    def top(self) -> int:
        return self.store.queue[-1][0]

    def getMin(self) -> int:
        return self.store.queue[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()