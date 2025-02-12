class Solution:
    def isMatch(self, s: str, p: str) -> bool:        
        # manual cache if not using @cache 
        # pair_match = {} # {(s index, p index): true/false}

        @cache # automatic cache, returns result if same params
        def backtrack(i, j):
            # if (i, j) in pair_match: # already checked pair
            #     return pair_match[(i, j)] 

            if j == -1: # p is empty, s must also be empty
                result = i == -1 

            elif i == -1: # s is empty and p isn't. all p[j] must be "*" since "*" can remove prev and "*"
                result = p[j] == '*' and backtrack(i, j - 2) # j - 2 to skip "*" and char it copies

            elif p[j] == '*': # can either stop using current "*" or match "*" to s[i]. 
                result = backtrack(i, j - 2) or (s[i] == p[j - 1] or '.' == p[j - 1]) and backtrack(i - 1, j)

            else: # check if current and prev pairs match
                result = (s[i] == p[j] or '.' == p[j]) and backtrack(i - 1, j - 1)

            # pair_match[(i, j)] = result # save pair result for memo
            return result

        return backtrack(len(s) - 1, len(p) - 1) # start at last chars