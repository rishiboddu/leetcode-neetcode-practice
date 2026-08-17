'''
Leetcode #14: Longest Common Prefix

given an array of strings, return the longest common case-insensitive prefix amongst all the elements, "" if there is none
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        elif len(strs) == 1:
            return strs[0]

        longestPrefix = strs[0]
        for currWord in strs[1:]:
            if len(longestPrefix) > len(currWord):
                longestPrefix = longestPrefix[0:len(currWord)]
            for i in range(len(longestPrefix)):
                if currWord[i] != longestPrefix[i]:
                    longestPrefix = longestPrefix[0:i]
                    break
        return longestPrefix
