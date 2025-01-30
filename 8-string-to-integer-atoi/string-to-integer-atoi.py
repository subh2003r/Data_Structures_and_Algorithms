# subhankar
class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1 
        ans = 0
        i,n = 0,len(s)
        maxi,mini = 2**31 - 1, -2**31
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0

        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1        

        while i < n:
            char = s[i]
            if ((char == ' ') or (not (char >= '0' and char <= '9'))):
                break
            ans = ans*10 + int(char)
            if sign == 1 and sign*ans > maxi:
                return maxi
            if sign == -1 and sign*ans < mini:
                return mini
            i += 1

        return sign*ans
            