'''
Leetcode #56 : Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort initial list by i[0] for each element i in intervals
        intervals.sort()

        i = 0
        while i < len(intervals) - 1:
            currRange = intervals[i]
            nextRange = intervals[i+1]
            # if the end of the currRange > start of nextRange, merge the two
            if currRange[1] >= nextRange[0]:
                intervals[i] = [currRange[0], max(currRange[1],nextRange[1])]
                intervals.pop(i+1)
                continue
            i += 1

        return intervals
