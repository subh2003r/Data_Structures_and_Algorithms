class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute approach 
        # Find all substrings 
        n = len(s)
        max_len = 0

        for i in range(n):
            store = set()
            count = 0
            for j in range(i, n):
                if s[j] in store:
                    # duplicate encountered
                    # no string can start with i uptil current j 
                    break
                count += 1
                store.add(s[j])
            
            max_len = max(max_len, count)

        return max_len