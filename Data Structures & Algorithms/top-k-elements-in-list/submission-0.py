class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n,0)

        arr = []
        for n,c in hashmap.items():
            arr.append([c,n])
        arr.sort()

        result = []
        while len(result) < k:
            result.append(arr.pop()[1])

        return result