class Solution:
    def __init__(self):
        self.store = []

    def checkValid(self,parenthesis):
        stack = []      
        mapping = {')':'('}

        for char in parenthesis:
            if char in mapping:
                top_element = stack.pop() if stack else 'x'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack

    def recur(self,newStr,n):
        if len(newStr) == n:
            self.store.append(newStr)
            return
        
        self.recur(newStr + "(",n)
        self.recur(newStr + ")",n)

    def generateParenthesis(self, n: int) -> List[str]:
        self.recur("",2*n)
        res = []

        for value in self.store:
            if self.checkValid(value):
                res.append(value)

        return res