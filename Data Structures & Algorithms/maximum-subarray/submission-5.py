class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best=nums[0]
        n=len(nums)
        current=0

        for i in range(n) :
            current += nums[i]
            if current < nums[i]:
                current = nums[i]
            if current > best :
                best=current
        return best

