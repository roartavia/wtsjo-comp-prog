# https://leetcode.com/problems/maximum-subarray/

#!/usr/bin/env python
# Brute force, all possible sums (sub arrays)
def maxSubArrayBrute(nums):
    newList = []
    new_start = 0
    newList.append(nums[0])
    for index in range(1, len(nums)):
        current_len = len(newList)

        for i in range(new_start, current_len):
            newList.append(nums[index] + newList[i])
        newList.append(nums[index])
        new_start = len(newList) - current_len
        new_start = len(newList) - new_start
    return max(newList)


def maxSubArrayRodolfo(nums):
    currentMAX = nums[0]
    futureMAX = currentMAX
    i = 1
    while (i < len(nums)):
        if futureMAX + nums[i] > nums[i]:
            futureMAX = futureMAX + nums[i]
        else:
            futureMAX = nums[i]
        if futureMAX > currentMAX:
            currentMAX = futureMAX
        i += 1
    return currentMAX


def maxSubArrayVictor(nums):
    prevSum = 0
    index = 0
    biggest = 0
    for num in nums:
        if index == 0:
            prevSum = num
            biggest = num
        else:
            newSum = prevSum + num
            if num > prevSum:
                if newSum > num:
                    prevSum = newSum
                else:
                    prevSum = num
            else:
                prevSum = newSum
        if prevSum > biggest:
            biggest = prevSum
        index += 1
    return biggest


nums = [5, 4, -1, 7, 8]
print(maxSubArrayRodolfo(nums))
