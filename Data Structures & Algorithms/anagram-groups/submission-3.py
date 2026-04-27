class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        satyam = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            satyam[tuple(count)].append(s)
        return list(satyam.values())