class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        # Brute force approach
        min_len = float("inf")
        start_index = -1
        n = len(s)
        m = len(t)

        for i in range(n):
            store = {}
            count = 0
            for j in range(m):
                store[t[j]] = store.get(t[j],0) + 1
            for j in range(i,n):
                if store.get(s[j],0) > 0:
                    count += 1
                store[s[j]] = store.get(s[j], 0) - 1
                if count == m:
                    if min_len > j-i+1:
                        min_len = j-i+1
                        start_index = i
                    break

        return "" if start_index == -1 else s[start_index:start_index+min_len]
        '''

        # Using sliding window approach
        n, m = len(s), len(t)
        left, right = 0, 0
        start_index = -1
        min_len = float("inf")
        store = {}
        count = 0

        for char in t:
            store[char] = store.get(char,0)+1

        while right < n:
            if store.get(s[right], 0) > 0:
                count += 1
            store[s[right]] = store.get(s[right],0) - 1

            while count == m:
                if min_len > right-left+1:
                    min_len = right-left+1
                    start_index = left
                
                store[s[left]] += 1
                if store[s[left]] > 0:
                    count -= 1
                left += 1

            right += 1

        return "" if start_index == -1 else s[start_index: start_index+min_len]