class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0

        for coin in bills:
            if coin == 5:
                five += 1
            elif coin == 10:
                if five:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:
                if five and ten:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False

        
        return True
