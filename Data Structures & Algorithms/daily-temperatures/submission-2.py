class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = deque()
        idx = deque()
        res = [0]*len(temperatures)
        for i, t in enumerate(temperatures):            
            while temps and t > temps[-1]:
                tl = temps.pop()
                t_id = idx.pop()
                res[t_id] = i-t_id
            temps.append(t)
            idx.append(i)

        return res
        