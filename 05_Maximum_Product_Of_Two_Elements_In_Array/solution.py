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
