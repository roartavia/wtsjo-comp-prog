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


def lengthOfLastWordVictor(s: str) -> int:
    stripped = s.strip()
    answer = ""
    for i in range(len(stripped)-1, -1, -1):
        char = stripped[i]
        if char == " ":
            break
        answer += stripped[i]
    return len(answer)

def lengthOfLastWordJuanCarlos(s: str) -> int:
    return len(s.split()[-1])

def lengthOfLastWordSebas(s):
        return len(s.split()[-1])
