class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [""]
        anagram_map = {}
        output = []
        for string in strs:
            ct = frozenset(Counter(string).items())
            if ct in anagram_map:
                anagram_map[ct].append(string)
            else:
                anagram_map[ct] = [string]
        return list(anagram_map.values())
              