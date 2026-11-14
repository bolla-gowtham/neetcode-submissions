class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x = sorted(numbers)
        l = 0
        r = len(x) - 1
        while l < r:
            s = x[l] + x[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return[l+1, r+1]
        return[]
                