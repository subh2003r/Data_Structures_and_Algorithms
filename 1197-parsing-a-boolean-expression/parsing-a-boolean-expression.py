from collections import deque

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = deque()

        def solveExpr(store, operator):
            if operator == '!':
                return 'f' if store[0] == 't' else 't'
            
            if operator == '&':
                for val in store:
                    if val == 'f':
                        return 'f'
                
                return 't'
            
            if operator == '|':
                for val in store:
                    if val == 't':
                        return 't'
                
                return 'f'
        

        for exp in expression:
            if exp == ',':
                continue

            if exp == ')':
                store = []
                while st and st[-1] != '(':
                    if st[-1] == 't' or st[-1] == 'f':
                        store.append(st[-1])
                        st.pop()
                
                st.pop() # remove the '(' bracket
                operator = st[-1]
                st.pop() # remove the operator

                st.append(solveExpr(store, operator))
            else:
                st.append(exp)
        
        return st[-1] == 't'


                

                    

