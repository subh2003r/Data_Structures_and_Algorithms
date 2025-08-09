class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        result = [[0]*n for _ in range(n)] 

        for i in range(n):
            for j in range(n):
                result[j][n-i-1] = matrix[i][j]
                
        for i in range(n):
            for j in range(n):
                matrix[i][j] = result[i][j]


        