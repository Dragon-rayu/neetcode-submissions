class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for s in strs:
            counterS=[0]*26
            for c in s:
                counterS[ord(c)-ord('a')]+=1
            result[tuple(counterS)].append(s)
        return list(result.values())
            
