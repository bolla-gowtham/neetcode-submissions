class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1]*(len(nums))
        pf = 1
        for i in range(len(nums)):
            arr[i] = pf
            pf *= nums[i]
        sf = 1
        for i in range(len(nums) - 1, - 1, - 1):
            arr[i] *= sf
            sf *= nums[i]
        return arr
            