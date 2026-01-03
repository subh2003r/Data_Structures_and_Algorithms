class Solution:
    def checkValidString(self, s: str) -> bool:
        # Greedy approach
        """
        We keep a range of possible open brackets instead of an exact count because * can act in multiple ways.
    If the maximum possible opens becomes negative, it means even the best interpretation has too many closing brackets, so the string is invalid.
    If only the minimum goes negative, we can adjust * to avoid that, so we clamp it to zero.
        """

        max_open, min_open = 0,0
        for ch in s:
            if ch == '(':
                min_open += 1
                max_open += 1
            elif ch == ')':
                min_open -= 1
                max_open -= 1
            else:
                # this condition is encountered during '*'
                min_open -= 1
                max_open += 1

            # this condition is only met when the string has more closing brackets than opening brackets
            if max_open < 0:
                return False

            if min_open < 0:
                min_open = 0
        
        # returns True when it is Valid string else False
        return min_open == 0

        """
        # Time complexity : O(3^k) where 'k' is the number of stars
        # recursive approach 

        def isValid(s, index, balance):
            if balance < 0:
                return False
            
            if index == len(s):
                return balance==0

            if s[index] == '(':
                return isValid(s, index+1, balance+1)
            if s[index] == ')':
                return isValid(s, index+1, balance-1)
            
            return (
                isValid(s, index+1, balance) or isValid(s, index+1, balance+1) or isValid(s, index+1, balance-1)
            )

            """