# https://leetcode.com/problems/length-of-last-word/

#!/usr/bin/env python
def lengthOfLastWordEasy(s: str) -> int:
    list_strs = s.split()
    if len(list_strs) == 0:
        return 0
    last = list_strs[-1]
    return len(last)


def lengthOfLastWordRodolfo(s: str) -> int:
    myLenght = 0
    latestIndex = len(s) - 1
    while latestIndex >= 0:
        if s[latestIndex] != " ":
            myLenght += 1
        else:
            if myLenght > 0:
                break
        latestIndex -= 1

    return myLenght
