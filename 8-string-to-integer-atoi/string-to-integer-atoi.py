# subhankar
class Solution:
    def myAtoi(self, s: str) -> int:
        '''
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
        '''

        n = len(s)
        index = 0
        res = 0
        sign = 1
        max_range, min_range = 2**31-1, -2**31

        # skip leading spaces
        while index < n and s[index] == ' ':
            index += 1
            
        # check the sign
        if index < n and (s[index] == '-' or s[index] == '+'):
            sign = -1 if s[index] == '-' else 1
            index += 1

        '''
        res * 10 + digit > max_range
        res > (max_range - digit) // 10 
        '''
        while index < n and s[index].isdigit():
            digit = int(s[index])
            
            if res > (max_range - digit) // 10:
                return max_range if sign == 1 else min_range

            res = res*10 + digit
            index += 1

        return sign*res