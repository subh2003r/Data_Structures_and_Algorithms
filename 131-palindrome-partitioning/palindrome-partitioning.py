class Solution:
    def __init__(self):
        self.store = []

    def isPalindrome(self,s):
        start,end = 0,len(s)-1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def recur(self,index,s,subPart):
        if index == len(s):
            self.store.append(subPart[:])
            return

        for i in range(index,len(s)):
            leftPart = s[index:i+1]
            if self.isPalindrome(leftPart):
                subPart.append(leftPart)
                self.recur(i+1,s,subPart)
                subPart.pop()

    def partition(self, s: str) -> List[List[str]]:
        self.recur(0,s,[])
        return self.store