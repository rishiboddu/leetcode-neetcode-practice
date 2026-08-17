'''
Leetcode #1209: Remove All Adjacent Duplicates in String II
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

Given string s and integer k, remove k adjacent and equal/duplicate letters from s, which consequentially causes the left and right sections of the deleted substring to concatenate together. 
Repeatedly make k duplicate removals from s until we no longer can. Return the final remaining string after all such k duplicate removals have been made.
'''

# approach : use a stack with [character, count] pairs to track adjacent duplicate characters even after k duplicate removals occur
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            # for each char in the string, add it to the stack as [character, count = 1]
            if not bool(stack) or stack[-1][0] != char:
                stack.append([char, 1])
            # if the current character is the same as the previous character on the stack, increase the count of the previous element
            else:
                stack[-1][1] += 1
                # if the count reaches k, pop that previous item
                if stack[-1][1] == k:
                    stack.pop()
        
        # build a string from what's left on our stack
        remainingString = ""
        for i in stack:
            remainingString += i[0] * i[1]
        return remainingString
