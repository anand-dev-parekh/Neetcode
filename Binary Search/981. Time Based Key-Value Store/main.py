class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((timestamp, value))
        else:
            self.map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.map: # Edge Case
            return "" 
        
        arr_ref = self.map[key]
        l, r = 0, len(arr_ref)-1

        # Bsearch
        while l < r:
            m = (l+r) // 2

            if arr_ref[m][0] >= timestamp:
                r = m
            else:
                l = m+1

        if arr_ref[l][0] > timestamp and l > 0: 
            l-=1

        return arr_ref[l][1] if arr_ref[l][0] <= timestamp else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)