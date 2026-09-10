class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for string in strs:
            counts = [0]*26
            for c in string:
                counts[ord("a")-ord(c)] += 1
            anagram_map[tuple(counts)].append(string)
        return list(anagram_map.values())
              