# https://leetcode.com/problems/plus-one/

#!/usr/bin/env python

class Solution:
    def plusOneRodolfo(self, digits):
        max = 9
        i = len(digits) - 1
        acarreo = False
        while (i >= 0):
            if digits[i] == max:
                digits[i] = 0
                acarreo = True
            else:
                digits[i] = digits[i] + 1
                # Process the corrimiento
                acarreo = False
                break
            i -= 1
        if acarreo:
            digits.insert(0, 1)
        return digits

    def plusOneVictor(self, digits):
        mySum = 0
        remainder = 1
        answer = []
        for i in range(len(digits)-1, -1, -1):
            digit = digits[i]
            digit += remainder
            if digit == 10:
                answer = [0]+answer
                remainder = 1
            else:
                answer = [digit]+answer
                remainder = 0
        if remainder > 0:
            return [remainder]+answer
        return answer


sol = Solution()
response = sol.plusOneRodolfo([9, 9])
print(response)
