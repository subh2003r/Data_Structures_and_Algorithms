from queue import LifoQueue
"""
class MinStack:
    
    # Time complexity: O(1)
    # Space complexity: O(2N) as we are storing pairs

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
"""

class MinStack:
    # Time complexity: O(1)
    # Space complexity: O(N)
    def __init__(self):
        self.mini = float("inf")
        self.store = LifoQueue()

    def push(self, val: int) -> None:
        if self.store.qsize() == 0:
            self.mini = val
            self.store.put(val)
        else:
            if val < self.mini:
                self.store.put(2*val-self.mini)
                self.mini = val
            else:
                self.store.put(val)

    def pop(self) -> None:
        if self.store.queue[-1] < self.mini:
            self.mini = 2*self.mini - self.store.queue[-1]
        
        self.store.get()    

    def top(self) -> int:
        if self.store.queue[-1] < self.mini:
            return self.mini

        return self.store.queue[-1]

    def getMin(self) -> int:
        return self.mini

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()