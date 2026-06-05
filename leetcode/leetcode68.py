'''
68. Text Justification
https://leetcode.com/problems/text-justification?envType=company&envId=notion&favoriteSlug=notion-more-than-six-months

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

'''
'''
edge case clarifying questions:

1. Can I assume the length of every element in words is <= maxwidth ?
2. Can the input list be empty? In this case should I just return an empty list
3. Can an element in words be empty? And in this case should I still treat it as an element and pad it with spaces ? 
4. Can I assume each element within words does not contain spaces? And if it does, do
    I need to format these spaces as well?

'''

'''
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        
        The problem can be broken into two tasks:
            Determine the maximum number of words that can fit into the current line.
            Distribute the remaining spaces according to the justification rules.
                Case 1: Normal line where all spaces are equally distributed
                Case 2: Final line - left justified, regular spacing


        Initial approach:
        traverse words, build a list of lists containing words to fit into each line
        traverse the new intermediate array and work on actually formatting spaces

        Time and space innefficient - O(n) time complexity scales with size of words,
        space inefficient to maintaing list of lists of strings

        

        pointer = 0
        charRemaining = maxWidth
        wordLines = []
        startIndex = 0
        endIndex = 0
        currLine = []

        while pointer < len(words):
            # if we have space on current line for current, word
            if charRemaining - len(words[pointer]) >= 0:
                # add to the list of words for this line, update pointer to next word
                currLine.append(words[pointer])
                charRemaining = charRemaining - 1 - len(words[pointer])
                pointer +=1
            # if this word does not fit 
            else:
                wordLines.append(currLine)
                currLine = []

        # go through intermediate list and now address formatting
        formatted = []
        for lineIndex in range(len(wordLines)):
            currLine = ""
            spaceRemaining = maxWidth - sum(len(i) for i in wordLines[line])
            spacesToAdd = spaceRemaining / len(wordLines[line])
            remainder = spaceRemaining % len(wordLines[line])
            for word in range(len(wordLines[line]) - 1):
                currLine += wordLines[line][word]
                currLine += " " * spacesToAdd
                if remainder > 0 and line < len(wordLines) - 1:
                    currLine += " "
                    remainder -= 1
            formatted.append(currLine)
        
        return formatted
'''
            

'''
Improvements to original approach:
Instead of doing two traversals, just do the formatting within the first traversal as well
No need to store a list of words in each line, I can just do it by having pointers to the indexes in the original list
'''
        


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        pointer = 0
        formatted = []

        while pointer < len(words):
            startWordIndex = pointer
            charRemaining = maxWidth

            # figure out words in line, at least one space between each word + len of words
            # (numWords - 1) + len(words) >= 0

            while pointer < len(words) and charRemaining - ((pointer - startWordIndex) + len(words[pointer])) >= 0:
                charRemaining -= len(words[pointer])
                pointer += 1

            
            # format the line for words [startWordIndex, pointer)
            currLine = ""
            wordsInLine = pointer - startWordIndex
            
            # case: only one word in the line
            if wordsInLine == 1:
                currLine += words[startWordIndex] + " " * (maxWidth - len(words[startWordIndex]))
            
            # case: last line
            elif pointer >= len(words):
                for i in range(startWordIndex, pointer - 1):
                    currLine += words[i]
                    currLine += " "
                # add trailing spaces after last word in last line
                currLine += words[pointer - 1]
                currLine += " " * (charRemaining - (wordsInLine - 1))

            else:
                spaceSize = charRemaining // (wordsInLine - 1)
                remainder = charRemaining % (wordsInLine - 1)
            
                for i in range(startWordIndex, pointer - 1):
                    currLine += words[i]
                    currLine += " " * spaceSize
                    if remainder > 0 :
                        currLine += " "
                        remainder -= 1                    

                currLine += words[pointer - 1]

            formatted.append(currLine)
        return formatted
