class Node:
    def __init__(self):
        self.children = [None, None]

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        self.root = Node()

        # build Trie :- O(31*N)
        for num in nums:
            node = self.root
            for shift in range(30, -1, -1):
                bit = (num >> shift) & 1
                if node.children[bit] is None:
                    node.children[bit] = Node()
                
                node = node.children[bit]
        
        # checking for the opposite bits in the trie -- O(31*N)
        for num in nums:
            node = self.root
            value = 0
            for shift in range(30, -1, -1):
                bit = (num >> shift) & 1
                opp = 1-bit
                if node.children[opp] is not None:
                    value |= (1 << shift)
                    node = node.children[opp]
                else:
                    node = node.children[bit]
            
            res = max(res, value)

        return res




