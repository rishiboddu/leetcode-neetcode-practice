'''
347. Top K Frequent Elements (medium)

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {}

        for element in nums:
            if element in frequencyMap:
                frequencyMap[element] += 1
            else:
                frequencyMap[element] = 1
        
        return sorted(frequencyMap, key=frequencyMap.get, reverse=True)[:k]
