'''
Leetcode #49: Group Anagrams (medium)
https://leetcode.com/problems/group-anagrams

given an array of strings, return an array of arrays grouping the anagrams together (any order)
'''

class Solution:
    # anagrams are words that have the same letters in diff order
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create dictionary, key = words with sorted ascending characters, values = list of all the anagrams that share the same sorted word
        anagramMap = {}

        # for each word in strs, sort its characters in ascending order
        for word in strs:
            sortedWord = "".join(sorted(word))
            anagramMap.setdefault(sortedWord, []).append(word)
        
        return list(anagramMap.values())
