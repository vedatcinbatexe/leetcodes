# 1464. Maximum Product of Two Elements in an Array
"""
You are given an array of integers nums.

Choose two different indices i and j of that array.

Return the maximum value of (nums[i] - 1) * (nums[j] - 1).

 

Example 1:

Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.

"""

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        mFirst, mSecond = 0, 0
        for num in nums:
            if(num > mFirst):
                mFirst, mSecond = num, mFirst
                continue
            if(num > mSecond):
                mSecond = num

        return (mFirst - 1) * (mSecond - 1)


sol = Solution()

print("Result: ", sol.maxProduct([3,4,5,2]))
print("Result: ", sol.maxProduct([10,2,5,2]))
print("Result: ", sol.maxProduct([3, 7]))
