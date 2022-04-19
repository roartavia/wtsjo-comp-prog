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


def maxSubArrayNatan(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_temp = 0
        max_current = -999999
        leng = len(nums)
        
        for i in range(leng):
            max_temp = max(nums[i], nums[i] + max_temp)
            
            if(max_temp > max_current):
                max_current = max_temp
                
        return max_current

def maxSubArrayJuanCarlos(nums):
    max_sum = nums[0]
    new_max = 0
        
    if len(nums) > 0:
        for number in nums:
            new_max = max(number, new_max + number)
            max_sum = max(new_max, max_sum)
    else:  
        # if the array is empty return 0
        max_sum = 0
        
    return max_sum


nums = [5, 4, -1, 7, 8]
print(maxSubArrayRodolfo(nums))
