class Node:
    def __init__(self, key, value, nextNode=None, prevNode=None):
        self.key = key
        self.value = value
        self.next = nextNode
        self.prev = prevNode

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.currentCapacity = 0
        self.store = {}
        # dummy head node
        self.head = Node(-1, -1)
        # dummy tail node
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addToFront(self, node):
        """ add new node after head and mark it as most recently used """
        nextNode = self.head.next
        node.prev = self.head
        node.next = nextNode
        self.head.next = node
        nextNode.prev = node

    def removeNode(self, node):
        """ remove node """
        nextNode = node.next
        prevNode = node.prev
        nextNode.prev = prevNode
        prevNode.next = nextNode

        node.next = node.prev = None

    def get(self, key: int) -> int:
        # if key is not present
        if key not in self.store:
            return -1

        node = self.store[key]
        self.removeNode(node)
        self.addToFront(node)

        return node.value
       
    def put(self, key: int, value: int) -> None:
        if key in self.store:
            node = self.store[key]
            node.value = value
            self.removeNode(node)
            self.addToFront(node)
            return

        # empty space if capacity is full
        if self.currentCapacity == self.capacity:
            node = self.tail.prev
            self.removeNode(node)

            # remove LRU key-value from dictionary
            del self.store[node.key]
            self.currentCapacity -= 1

        node = Node(key,value)
        self.addToFront(node)

        # add new key-value pair in dictionary
        self.store[node.key] = node
        self.currentCapacity += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)