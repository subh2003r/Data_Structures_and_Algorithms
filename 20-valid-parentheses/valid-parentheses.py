from queue import LifoQueue

class Solution:
    def isValid(self, s: str) -> bool:
        stack = LifoQueue()

        for char in s:
            if char in "({[":
                stack.put(char)
            else:
                if stack.qsize() == 0:
                    return False
                top_char = stack.queue[-1]
                if char == ')' and top_char == '(':
                    stack.get()
                elif char == '}' and top_char == '{':
                    stack.get()
                elif char == ']' and top_char == '[':
                    stack.get()
                else:
                    return False
        
        return True if stack.qsize() == 0 else False