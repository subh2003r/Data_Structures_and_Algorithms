import heapq
class MedianFinder:

    def __init__(self):
        self.left = [] # maxHeap
        self.right = [] # minHeap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        # left should contain all smaller elements and right should contain larger elements
        if self.right and (-self.left[0] > self.right[0]):
            value = -(heapq.heappop(self.left)) 
            heapq.heappush(self.right, value)
        
        if len(self.left)-len(self.right) > 1:
            value = -(heapq.heappop(self.left))
            heapq.heappush(self.right, value)
        elif len(self.right) > len(self.left):
            value = heapq.heappop(self.right)
            heapq.heappush(self.left, -value)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        
        return (-self.left[0] + self.right[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()