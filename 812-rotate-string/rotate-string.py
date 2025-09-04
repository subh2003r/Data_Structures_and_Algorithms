class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # new variable taken to prevent modifying new string
        rotated_str = s
        n = len(s)

        for i in range(n):
            if rotated_str == goal:
                return True
            rotated_str = rotated_str[n-1:n] + rotated_str[0:n-1]
        
        return False
