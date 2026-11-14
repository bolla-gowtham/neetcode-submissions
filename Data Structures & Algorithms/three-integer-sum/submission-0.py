from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort to enable two-pointer strategy
        
        for i, a in enumerate(nums):
            # Optimizations: if current element > 0, triplets can never sum to 0
            if a > 0:
                break
                
            # Skip duplicates for the first element
            if i > 0 and a == nums[i-1]:
                continue
                
            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # FIX: Boundary check must come first, skip duplicates safely
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                        
        return res
