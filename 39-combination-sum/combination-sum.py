class Solution:
    def __init__(self):
        self.store = []

    def recur(self, candidates, target, subSeq,index):
        if index == len(candidates):
            if target == 0:
                self.store.append(subSeq[:])
            return

        if candidates[index] <= target:
            subSeq.append(candidates[index])
            self.recur(candidates,target - candidates[index],subSeq,index)
            subSeq.pop()

        self.recur(candidates,target,subSeq,index+1)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.recur(candidates,target,[],0)
        
        return self.store