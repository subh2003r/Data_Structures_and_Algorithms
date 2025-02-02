class Solution:
    def __init__(self):
        self.res = []
    def recur(self,index,digits,store,comb):
        if index == len(digits):
            self.res.append(comb) # since string is immutable so no need to copy its character
            return
        data = store[digits[index]]
        for char in data:
            self.recur(index+1,digits,store,comb+char)

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        store = {'2':"abc",'3':"def",'4':"ghi",
        '5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        
        self.recur(0,digits,store,"")
        return self.res
