class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_of_digits = 1
        sum_of_digits =0
        for digit in str(n):
            product_of_digits = product_of_digits * int(digit)
            sum_of_digits = sum_of_digits + int(digit)
        return product_of_digits - sum_of_digits
        