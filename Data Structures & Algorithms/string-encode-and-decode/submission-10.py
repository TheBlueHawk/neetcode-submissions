class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for string in strs:
            encoding +=  chr(ord("a")+len(string)) + string
        return encoding

    def decode(self, s: str) -> List[str]:
        output = []
        idx = 0
        while idx < len(s):
            letter = s[idx]
            length = ord(letter) - ord("a") + 1
            output.append(s[idx+1:idx+length])
            idx += length
        return output