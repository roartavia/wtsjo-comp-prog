# https://leetcode.com/problems/add-binary

#!/usr/bin/env python

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


sol = Solution()
print(sol.addBinaryRodolfo("1010", "1011"))
print(sol.addBinaryCheating("1010", "1011"))
print(sol.addBinaryVictor("1010", "1011"))
