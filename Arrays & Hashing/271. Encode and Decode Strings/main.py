class Solution:
    def encode(self, strs: list[str]) -> str:

        res = ""
        for s in strs:
            size = len(s)
            res += str(size) + "#" + s

        return res

    def decode(self, s: str) -> list[str]:

        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            size = int(s[i:j])

            res.append(s[j+1:j+size+1])
            i = j + size + 1

        return res
