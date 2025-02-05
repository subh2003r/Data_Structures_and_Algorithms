class Solution:      
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        def solve(index,expression,result_so_far,prev_operand):
            if index == len(num):
                if result_so_far == target:
                    result.append(expression)
                return
            
            for i in range(index,len(num)):
                subStr = num[index:i+1]       # extract the substring
                operand = int(subStr)
                if len(subStr) > 1 and subStr[0] == '0':
                    break
                if index == 0:
                    # first operand no operator before it 
                    solve(i+1,expression+subStr,result_so_far+operand,operand)
                else:
                    # Addition
                    solve(i+1,expression+"+"+subStr,result_so_far+operand,operand)
                    # Substraction
                    solve(i+1,expression+"-"+subStr,result_so_far-operand,-operand)
                    # Multiplication
                    new_result = result_so_far - prev_operand + (prev_operand*operand)
                    solve(i+1,expression+"*"+subStr,new_result,prev_operand*operand)
        
        solve(0,"",0,0)

        return result
                    