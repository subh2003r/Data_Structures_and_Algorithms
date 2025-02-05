class Solution:
    def __init__(self):
        self.store = {}
        self.memo = {} # memoization dictionary

    def recur(self,s,index):
        if index == len(s):
            return True
        
        if index in self.memo:
            return self.memo[index]

        for i in range(index,len(s)):
            subStr = s[index:i+1]
            if ((subStr in self.store) and (self.recur(s,i+1))):
                self.memo[index] = True
                return True
        
        self.memo[index] = False
        return False
            
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.store = {val for val in wordDict}
        self.memo = {} # reset memoization dictionary
        return self.recur(s,0)