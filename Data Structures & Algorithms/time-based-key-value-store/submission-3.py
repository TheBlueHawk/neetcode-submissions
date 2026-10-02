class TimeMap:

    def __init__(self):
        self.kv = {}    

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.kv:
            self.kv[key].append((timestamp, value))
        else:
            self.kv[key] = [(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.kv.get(key, None)
        if not values:
            return ""

        l, r = 0, len(values) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if timestamp == values[mid][0]:
                return values[mid][1]
            elif timestamp < values[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
        if values[r][0] < timestamp:
            return  values[r][1]
        else:
            return "" 