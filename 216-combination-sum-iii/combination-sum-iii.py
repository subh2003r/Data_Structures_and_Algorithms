class Solution:
    def __init__(self):
        self.store = []
        self.limit = 0

    def recur(self,target,arr,index,subSeq):
        if target == 0 and len(subSeq) == self.limit:
            self.store.append(subSeq[:])
            return
        
        for i in range(index,len(arr)):
            if arr[i] > target or len(subSeq) >= self.limit:
                break
            subSeq.append(arr[i])
            self.recur(target-arr[i],arr,i+1,subSeq)
            subSeq.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        target = n
        arr = [1,2,3,4,5,6,7,8,9]
        self.limit = k
        self.recur(target,arr,0,[])
        return self.store