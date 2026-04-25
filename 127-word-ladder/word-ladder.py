from collections import defaultdict, deque

class Solution:
    def non_optimized_approach(self, beginWord, endWord, wordList):
        # we use BFS, as shortest path -- transformation is required 
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        dq = deque([(beginWord, 1)]) # word, path

        while dq:
            word, level = dq.popleft()
            if word == endWord:
                return level 

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + ch + word[i+1:]

                    if newWord in wordSet:
                        dq.append((newWord, level+1))
                        wordSet.remove(newWord) # mark visited 
        
        return 0

    def optimized_pattern_approach(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        dq = deque([(beginWord, 1)])
        # building patterns 
        pattern_map = defaultdict(list)

        visited = set([beginWord])

        # create patterns and append words to it 
        for word in wordList:
            for index in range(len(word)):
                pattern = word[:index] + "*" + word[index+1:]
                pattern_map[pattern].append(word)

        while dq:
            word, level = dq.popleft()

            if word == endWord:
                return level

            for index in range(len(word)):
                pattern = word[:index] + "*" + word[index+1:]

                for neighb in pattern_map[pattern]:
                    if neighb not in visited:
                        dq.append((neighb, level+1))
                        visited.add(neighb)
                
                # optimization -- to prevent iterating the neighbours for the same pattern already processed 
                pattern_map[pattern] = []

        return 0

    def final_optimized(self, beginWord, endWord, wordList):
        """
        Suppose branching factor is 'b' and depth is 'd', Normal BFS would visit almost b^d nodes, but if we use bidirectional BFS, i.e traversing from both start and the end such that size of both remains same .. then overall nodes traversed would be 2 * (b^(d/2))

        Here we use two sets, and not deque unlike the deque 
        because deque processed node by node and sets processes level by level 
        Time complexity although looks same .. but is greatly reduced because of less node traversing
        """

        # Time complexity and search behaviour
        """
        Time complexity is O(N × L × 26) since for each word we try all possible one-letter transformations. However, the actual search behaves like O(b^d), which is why bidirectional BFS is used to reduce it to O(b^(d/2)).
        """
        wordSet = set(wordList)
        # if endword is not present in wordSet
        if endWord not in wordSet:
            return 0

        beginSet, endSet = {beginWord}, {endWord}
        visited = set([beginWord, endWord])

        """
        beginSet and endSet condition is used because if either of them is empty then it wont be possible to reach from start to end 
        """
        steps = 1

        while beginSet and endSet:
            # next_level variable contains all the words which will be traversed in the next set
            next_level = set()

            # figure out which is bigger in length 
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet

            for word in beginSet:
                for index in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:index] + ch + word[index+1:]

                        # if new_word is in other set i.e. endSet, then we were able to connect both the beginWord and endWord
                        if new_word in endSet:
                            return steps + 1

                        if new_word in wordSet and new_word not in visited:
                            visited.add(new_word)
                            next_level.add(new_word)

            beginSet = next_level
            steps += 1                      

        return 0  

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # return self.non_optimized_approach(beginWord, endWord, wordList)
        # return self.optimized_pattern_approach(beginWord, endWord, wordList)
        return self.final_optimized(beginWord, endWord, wordList)
        