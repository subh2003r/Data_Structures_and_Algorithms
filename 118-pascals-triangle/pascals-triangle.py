class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        if numRows == 1:
            return res
        numRows -= 1
        
        while numRows:
            num_res = res[-1]
            interim_res = [1]
            for i in range(1, len(num_res)):
                interim_res.append(num_res[i]+num_res[i-1])
            interim_res.append(1)

            res.append(interim_res)

            numRows -= 1

        return res