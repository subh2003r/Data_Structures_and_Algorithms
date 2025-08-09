class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        # Brute force approach 

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
        '''

        '''
        # this is similar to combination 
        nCr = nC0 + nC1 + nC2 + .... + nCr-1
        # Given n = 5, find the r=3 term

        def findNcr(n,r):
            res = 1
            for i in range(r):
                res *= (n-i)
                res //= (i+1)
            
            return res

        # Find n = 5 pascals value
        
        res = 1
        final_value = [1]

        for r in range(1,n):
            res *= (n-r)
            res //= r
            
            fina_value.append(res)
        '''

        final_result = []

        for row in range(1, numRows+1):
            interim_result = [1]
            ans = 1
            for col in range(1, row):
                ans *= (row-col)
                ans //= col
                interim_result.append(ans)      
                  
            final_result.append(interim_result)

        return final_result