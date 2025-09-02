class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        words = s.strip().split()
        words.reverse()

        return " ".join(words) 
        '''

        n = len(s)
        end = n-1
        res = ""

        while end >= 0:
            while end >= 0 and s[end] == " ":
                end -= 1

            if end < 0:
                break
            
            word = ""
            while end >= 0 and s[end] != " ":
                word += s[end]
                end -= 1


            res += word[::-1] + " "

        return res.strip()
            