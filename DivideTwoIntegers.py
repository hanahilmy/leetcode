class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        negative = (dividend < 0) ^ (divisor < 0)
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        result = 0
        while abs_dividend >= abs_divisor:
            temp, multiple = abs_divisor, 1
            while abs_dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            abs_dividend -= temp
            result += multiple
        result = -result if negative else result
        return max(INT_MIN, min(INT_MAX, result))

solution = Solution()
print(solution.divide(10, 3)) 
print(solution.divide(7, -3))  
print(solution.divide(0, 1))   
print(solution.divide(1, 1))   
