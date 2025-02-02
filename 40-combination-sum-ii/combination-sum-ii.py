class Solution:
    def __init__(self):
        # self.store = set()
        self.store = []
    '''
    # brute force recursive approach

    def recur(self,candidates,target,index,subSeq):
        if index == len(candidates):
            if target == 0:
                self.store.add(subSeq)
            return
            
        # creating a new tuple everytime this function is called
        
        self.recur(candidates,target-candidates[index],index+1,subSeq+(candidates[index],))
        self.recur(candidates,target,index+1,subSeq)
    '''

    def recur(self,index,candidates,target,subSeq):
        if target == 0:
            self.store.append(subSeq[:])
            return
        
        for i in range(index,len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target:
                break
            subSeq.append(candidates[i])
            self.recur(i+1,candidates,target-candidates[i],subSeq)
            subSeq.pop()
            

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        # brute force recursive approach

        candidates.sort()
        self.recur(candidates,target,0,())
        return [list(subSeq) for subSeq in self.store]
        '''

        candidates.sort()
        self.recur(0,candidates,target,[])

        return self.store

