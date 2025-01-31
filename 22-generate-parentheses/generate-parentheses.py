class Solution:
    def __init__(self):
        self.store = []

    def recur(self,newStr,m,n,open,close):
        if close > open:
            return
        if len(newStr) == m:
            self.store.append(newStr)
            return
        if open < n:
            self.recur(newStr + "(",m,n,open+1,close)
        if close < n:
            self.recur(newStr + ")",m,n,open,close+1)

    def generateParenthesis(self, n: int) -> List[str]:
        self.recur("",2*n,n,0,0)
        return self.store