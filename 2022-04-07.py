# https://leetcode.com/problems/search-insert-position/

#!/usr/bin/env python

def getInsertPositionRodolfo(nums, target: int):
    # out: 2
    corrimiento = 0
    while len(nums) > 0:
        middle = len(nums)//2
        if nums[middle] == target or middle == 0:
            # you have the target no need to increase the corrimiento
            if middle != 0:
                corrimiento += middle
            if nums[middle] < target:
                corrimiento += 1
            break
        if target > nums[middle]:
            # move to the right, corrimiento increases by the middle (?)
            corrimiento += middle
            nums = nums[middle:]
        else:
            # move to the left, no need to do anything to the corrimiento
            nums = nums[:middle]
    return corrimiento


nums = [1, 3, 5, 6]
target = 2
print(getInsertPositionRodolfo(nums, target))
