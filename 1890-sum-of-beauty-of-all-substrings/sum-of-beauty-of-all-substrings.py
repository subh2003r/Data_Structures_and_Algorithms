class Solution:
    def beautySum(self, s: str) -> int:
        total_beauty = 0
        n = len(s)

        for i in range(n):
            store_freq = [0]*26
            for j in range(i,n):
                index = ord(s[j]) - ord('a')
                store_freq[index] += 1

                max_freq = max(store_freq)
                min_freq = min(freq for freq in store_freq if freq > 0)

                total_beauty += (max_freq - min_freq)

        return total_beauty
                