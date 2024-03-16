from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        -> iterate right ptr
            find window map which contains t

        -> iterate left ptr till
            find window till it doesn't exist
        """

        # Set up t char:freq map
        t_map = {}
        for c in t:
            if c in t_map:
                t_map[c] += 1
            else:
                t_map[c] = 1


        # Start Sliding Window
        min_window, ans = 1000000, (0, 0)
        cur_matches, goal_matches = 0, len(t_map.keys())
        window_map = defaultdict(lambda: 0)

        left_ptr, right_ptr = 0, 0
        for right_ptr in range(len(s)):
            cr = s[right_ptr]

            if cr not in t_map: # ignore any chars not in t
                continue

            window_map[cr] += 1
            if window_map[cr] == t_map[cr]: # Check if new match
                cur_matches += 1

            # Shift left over until matches isn't goal
            while cur_matches == goal_matches:
                cl = s[left_ptr]

                if right_ptr-left_ptr < min_window:
                    min_window = right_ptr - left_ptr
                    ans = (left_ptr, right_ptr+1)

                if cl in t_map and window_map[cl] == t_map[cl]:
                    cur_matches -= 1

                if cl in t_map:
                    window_map[cl] -= 1
                left_ptr += 1

        return s[ans[0]:ans[1]]
