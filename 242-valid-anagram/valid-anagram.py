class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # time complexity -> O(n) and space complexity -> O(26) atmost 26 alphabets -> O(1)
        def check():
            store_cnt = {}
            for char in s:
                store_cnt[char] = store_cnt.get(char,0) + 1
            
            for char in t:
                if char in store_cnt and store_cnt[char] > 0:
                    store_cnt[char] -= 1
                else:
                    return False

            return True if sum(store_cnt.values()) == 0 else False

        return len(s) == len(t) and check()