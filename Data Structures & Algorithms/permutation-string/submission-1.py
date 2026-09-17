class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = {}
        for c in s1:
            d1[c] = 1 + d1.get(c, 0)
        
        d2 = {}
        for c in s2[:len(s1)]:
            d2[c] = 1 + d2.get(c,0)
        
        for i in range(len(s1),len(s2)):
            print(d2)
            if d1 == d2:
                return True
            
            cl, cr = s2[i-len(s1)], s2[i]
            d2[cl] -= 1
            if d2[cl] == 0:
                d2.pop(cl)
            d2[cr] = 1 + d2.get(cr, 0)
        if d1 == d2:
                return True
        return False