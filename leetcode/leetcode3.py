'''
Leetcode #3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string s, find the length of the longest substring without duplicate characters.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring (adjacent occuring characters), "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        previous_length = 0
        max_length = 0

        for i in range(len(s)):
            char = s[i]
            previous_start = i - previous_length

            if char not in last_seen or last_seen[char] < previous_start:
                current_length = previous_length + 1
            else:
                current_length = i - last_seen[char]

            last_seen[char] = i
            previous_length = current_length
            max_length = max(max_length, current_length)

        return max_length

'''
Inefficiencies in the approach below:
1. Space inefficient because new set is being created with every iteration of outer loop: O(n)
2. Time inefficient because we are using a nested for loop so we're running the program n^2 times

Address both by using a single set and pointers to a window of letters that expands
'''
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstringLen = 0
        for i in range(len(s)):
            chars = set()
            for j in range(i, len(s)):
                if s[j] in chars:
                    break
                else:
                    chars.add(s[j])
            print(chars)
            if len(chars) > longestSubstringLen:
                longestSubstringLen = len(chars)
        return longestSubstringLen
'''
