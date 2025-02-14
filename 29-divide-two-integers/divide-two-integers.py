def divide(a, b):
    if a == -2**31 and b == -1:
        return 2**31 - 1
    sign = -1 if (a < 0) ^ (b < 0) else 1
    a = abs(a)
    b = abs(b)

    quotient = 0

    for i in range(31, -1, -1):

        if (b << i) <= a:
            a -= (b << i)
            quotient |= (1 << i)

    return sign * quotient

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return divide(dividend,divisor)