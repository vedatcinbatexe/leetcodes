"""
2206. Divide Into Array Into Equal Pairs

You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.

 

Example 1:

Input: nums = [3,2,3,2,2,2]
Output: true
Explanation: 
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.
"""


# My Solution
class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        pairs = len(nums) / 2
        pairCount = 0
        
        visited = [False] * len(nums)
        
        print(visited)
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if((nums[i] == nums[j]) and (visited[i] == False and visited[j] == False)):
                    pairCount += 1
                    visited[i] = True
                    visited[j] = True
        
        return pairs == pairCount

# Recommended Solution
class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        res = set()
        for n in nums:
            if n in res:
                res.remove(n)
            else:
                res.add(n)
        return len(res) == 0