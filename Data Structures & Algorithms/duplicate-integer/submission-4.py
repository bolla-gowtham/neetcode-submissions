class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums) == 1:
            return False
        for n in range (0,len(nums)):
            if nums[n] == nums[n-1]:
                return True
        return False