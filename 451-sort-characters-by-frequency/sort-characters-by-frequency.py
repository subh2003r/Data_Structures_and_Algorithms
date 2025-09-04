class Solution:
    def frequencySort(self, s: str) -> str:
        '''
        # we right key = values, i.e based on values we should sort, reverse = True means descending order
        freq = {'t': 1, 'r': 1, 'e': 2}
        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        '''

        # bucket sort
        '''
        Time:
            Counting: O(n)
            Bucket creation & filling: O(k) (k = number of unique characters)
            Rebuilding string: O(n)
            Total: O(n)

        Space: O(n) for buckets and result.
        '''

        store_dict = {}
        res = ""
        # counting freq
        for char in s:
            store_dict[char] = store_dict.get(char,0) + 1

        max_freq = max(store_dict.values())
        
        # creating bucket (for 'k' unique chars)
        bucket = [[] for _ in range(max_freq+1)]

        for char, freq in store_dict.items():
            bucket[freq].append(char)

        for freq in range(max_freq, 0, -1):
            # as many char can be present in a bucket of given freq
            for char in bucket[freq]:
                res += char*freq

        return res
