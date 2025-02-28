#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        m,n = len(a),len(b)
        union = []
        left,right = 0,0
        
        while left < m and right < n:
            while left > 0 and left < m and a[left] == a[left-1]:
                left += 1
            
            while right > 0 and right < n and b[right] == b[right-1]:
                right += 1
            
            if left < m and right < n:
                if a[left] == b[right]:
                    union.append(a[left])
                    left,right = left+1,right+1
            
                elif a[left] < b[right]:
                    union.append(a[left])
                    left += 1
                
                else:
                    union.append(b[right])
                    right += 1
        
        while left < m:
            if left == 0 or a[left] != a[left-1]:
                union.append(a[left])
            left += 1
        
        while right < n:
            if right == 0 or b[right] != b[right-1]:
                union.append(b[right])
            right += 1
        
        return union

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        li = ob.findUnion(a, b)
        for val in li:
            print(val, end=' ')
        print()
        print("~")

# } Driver Code Ends