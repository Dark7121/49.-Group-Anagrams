class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new = {}
        for i in strs:
            temp = ''.join(sorted(i))
            if temp in new:
                new[temp].append(i)
            else:
                new[temp] = [i]
        return new.values()
