class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [[] for _ in range(len(s) + 1)]
        dp[0] = [""]  # Base case: start with an empty sentence
        
        for i in range(len(s)):
            if not dp[i]:  # Only proceed if there are valid sentences at dp[i]
                continue
            for word in wordDict:
                if s[i:i + len(word)] == word:
                    for sentence in dp[i]:
                        if not sentence: # first word
                            dp[i + len(word)].append(word)
                        else:
                            dp[i + len(word)].append((sentence + " " + word))
        
        return dp[len(s)]