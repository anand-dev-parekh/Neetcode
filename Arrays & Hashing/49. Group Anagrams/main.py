class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        s_map = {}
        for s in strs:

            s_sorted = ''.join(sorted(s))
            if s_sorted in s_map:
                s_map[s_sorted].append(s)
            else:
                s_map[s_sorted] = [s]

        return [x for x in s_map.values()]
