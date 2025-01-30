# subhankar
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip() # removing leading white spaces
        if not s:
            return 0
        sign = 1
        maxi,mini = 2**31 - 1, -2**31
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        def conversion(num,index):
            if index == len(s) or not s[index].isdigit():
                return sign*num

            value = int(s[index])
            num = num*10 + value

            if sign == 1 and sign*num > maxi:
                return maxi
            if sign == -1 and sign*num < mini:
                return mini
            
            return conversion(num,index+1)
        
        return conversion(0,0)