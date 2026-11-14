class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        smap = {}
        tmap = {}
        for n in s:
            smap[n] = smap.get(n,0)+1
        for n in t:
            tmap[n] = tmap.get(n,0) + 1
        return smap == tmap 