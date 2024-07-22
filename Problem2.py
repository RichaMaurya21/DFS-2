## Problem2 (https://leetcode.com/problems/decode-string/)
class Solution:
    def decodeString(self, s: str) -> str:
        charStack = []
        digitStack = []
        currNum = 0
        currString = ""

        for i in s: 
            if i.isdigit():
                currNum = currNum * 10 + int(i)
            # when i == "["
            # Add digit to digitStack, 
            # Add parent i.e currentString to character stack and 
            # Reset the currnum and currSting
            elif i == "[":
                digitStack.append(currNum)
                charStack.append(currString)
                currNum = 0
                currString = ""

            elif i == "]":
                count = digitStack.pop()
                childStr = currString * count
                parent = charStack.pop()
                currString = parent + childStr

            else:
                currString += i

        return currString

            
