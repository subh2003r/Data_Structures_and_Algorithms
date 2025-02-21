class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix:
            ans.extend(matrix.pop(0))  # Take the first row
            if matrix:
                matrix = [list(row) for row in zip(*matrix)][::-1]  # Rotate counterclockwise
        return ans