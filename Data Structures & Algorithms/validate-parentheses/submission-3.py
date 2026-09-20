class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False

        close_matches = {")":"(", "]":"[","}":"{"}
         
        dq = deque()
        for i, c in enumerate(s):
            if c in close_matches:
                if len(dq) == 0:
                    return False
                last_open = dq.pop()
                if close_matches[c] != last_open:
                    return False
            else:
                dq.append(c)      
        return len(dq) == 0