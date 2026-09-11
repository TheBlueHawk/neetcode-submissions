class Solution:

    def encode(self, strs: List[str]) -> str:
        payload = "".join(strs)
        decode_key = [chr(ord("a")-1)]*200
        for i, string in enumerate(strs):
            decode_key[i] = chr(ord("a") + len(string))
        encoding = "".join(decode_key) + payload
        print(encoding)
        return encoding

    def decode(self, s: str) -> List[str]:
        decode_key = s[:200]
        output = []
        idx = 200
        for letter in decode_key:
            if letter == chr(ord("a")-1):
                return output
            length = ord(letter) - ord("a")
            output.append(s[idx:idx+length])
            idx += length
