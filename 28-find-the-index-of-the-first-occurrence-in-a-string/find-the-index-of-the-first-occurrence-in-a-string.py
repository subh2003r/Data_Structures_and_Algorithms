class Solution:
    def bruteForce(self, haystack, needle):
        # find all occurences of needle first character in haystack 
        occur = []
        n, m = len(haystack), len(needle)
        for i in range(n):
            if haystack[i] == needle[0]:
                occur.append(i)
        
        for idx in occur:
            limit = idx + m
            start = 0
            j = idx
            while idx < limit and start < m and idx < n:
                if haystack[idx] == needle[start]:
                    idx += 1
                    start += 1
                else:
                    break
            
            if start == m:
                return j

        return -1

    def strStr(self, haystack, needle):
        return self.bruteForce(haystack, needle)