# https://leetcode.com/problems/add-binary

#!/usr/bin/env python
import math

class Solution:
    # Doesn't make sense to do this solution because the idea is to use problem solving thinking
    # not only the language features
    def addBinaryCheating(self, a: str, b: str) -> str:
        return "{0:b}".format((int(a, base=2) + int(b, base=2)))

    # With list
    def addBinaryRodolfo(self, a: str, b: str) -> str:
        maxim = list(a)
        minim = list(b)

        if (len(a) < len(b)):
            maxim = list(b)
            minim = list(a)
        acarreo = False
        index = len(minim) - 1
        indexY = len(maxim) - 1

        while indexY >= 0:
            if index >= 0:
                if minim[index] == "1" and minim[index] == maxim[indexY]:
                    if acarreo:
                        maxim[indexY] = "1"
                    else:
                        maxim[indexY] = "0"
                    acarreo = True
                elif minim[index] == "1":
                    if acarreo:
                        maxim[indexY] = "0"
                        acarreo = True
                    else:
                        maxim[indexY] = "1"
                        acarreo = False
                elif maxim[indexY] == "1":
                    if acarreo:
                        maxim[indexY] = "0"
                        acarreo = True
                    else:
                        acarreo = False
                else:
                    # min 0
                    if acarreo:
                        maxim[indexY] = "1"
                        acarreo = False
            else:
                if acarreo:
                    if maxim[indexY] == "1":
                        maxim[indexY] = "0"
                        acarreo = True
                    else:
                        maxim[indexY] = "1"
                        acarreo = False
                else:
                    break
            index -= 1
            indexY -= 1

        if acarreo:
            maxim.insert(0, "1")

        return ''.join(maxim)

    def addBinaryVictor(self, a: str, b: str):
        shortest = a
        longest = b
        if len(b) < len(a):
            shortest = b
            longest = a
        i = len(shortest) - 1
        j = len(longest) - 1
        answer = ""
        remainder = 0
        while j >= 0:
            iElement = 0
            if i >= 0:
                iElement = shortest[i]
            jElement = longest[j]
            tempSum = int(iElement) + int(jElement) + remainder
            if tempSum == 3:
                answer = "1" + answer
                remainder = 1
            elif tempSum == 2:
                answer = "0" + answer
                remainder = 1
            else:
                answer = str(tempSum) + answer
                remainder = 0
            i -= 1
            j -= 1
        if remainder == 1:
            answer = str(remainder) + answer
        return answer

    def addBinaryJuanCaMathError(self, a: str, b: str) -> str:
            firstBinArray = list(a)
            secondBinArray = list(b)
            
            lenOne = len(firstBinArray) - 1
            lenTwo = len(secondBinArray) - 1
            
            intOne = 0
            intTwo = 0
            quotient = 1
            binResult = ""
            
            for bin in firstBinArray:
                intOne += int(bin)*(math.pow(2, (lenOne))) 
                lenOne -= 1
                
            for bin in secondBinArray:
                intTwo += int(bin)*(math.pow(2, (lenTwo)))
                lenTwo -= 1
                                
            intResult = intOne + intTwo
                    
            while quotient != 0:
                quotient = int(intResult // 2)
                remainder = int(intResult % 2)
                binResult = str(remainder) + binResult
                intResult = quotient
            
            return binResult

            
    def addBinarySebas(self, a: str, b: str) -> str:
        remainder = 0
        iA = len(a)-1
        iB = len(b)-1
        res = ""
        while iA >= 0 or iB >= 0 or remainder >= 0:
            if iA >= 0:
                num1 = a[iA]
            else:
                num1 = 0
                
            if iB >= 0:
                num2 = b[iB]
            else:
                num2 = 0
            sum = int(num1) + int(num2) + remainder
            if sum >= 2:
                remainder = 1
            else:
                remainder = 0
                
            res = str(sum%2) + res
                
            if iA <= 0 and iB <= 0 and remainder == 0:
                remainder = -1
            iA -= 1
            iB -= 1
        return res

    def addBinaryJuanCaTwo(self, a: str, b: str) -> str:
        firstBinArray = list(a)
        secondBinArray = list(b)
        result = ""
        carryDigit = 0
        
        if len(firstBinArray) > len(secondBinArray):
            maxLen = len(firstBinArray)
            maxBin = firstBinArray
            minBin = secondBinArray
        else:
            maxLen = len(secondBinArray)
            maxBin = secondBinArray
            minBin = firstBinArray 
        
        while maxLen > len(minBin):
            minBin.insert(0, '0')
        
        index = maxLen - 1
        for i in range(maxLen):
            tempDigit = carryDigit
            if maxBin[index] == "1":
                tempDigit += 1
                
            if minBin[index] == "1":
                tempDigit += 1 
            index -= 1

            if tempDigit % 2 == 1:
                result = '1' + result
            else:
                result = '0' + result

            carryDigit = 1 if tempDigit >= 2 else 0
                
        if carryDigit != 0:
            result = "1" + result
        
        return result

sol = Solution()
print(sol.addBinaryRodolfo("1010", "1011"))
print(sol.addBinaryCheating("1010", "1011"))
print(sol.addBinaryVictor("1010", "1011"))
print(sol.addBinaryJuanCaMathError("1010", "1011"))
print(sol.addBinaryJuanCaTwo("1010", "1011"))
