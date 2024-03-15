class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Edge case, impossible
        if len(s1) > len(s2):
            return False

        # Set up Maps
        s1_map = [0] * 26
        s2_map = [0] * 26
        for i in range(len(s1)):
            s2_map[ord(s2[i])-97] += 1
            s1_map[ord(s1[i])-97] += 1

        #Get Matches
        matches = 0
        for i in range(26):
            if s1_map[i] == s2_map[i]:
                matches += 1
        if matches == 26:
            return True

        # Sliding Window
        left_ptr = 0
        for right_ptr in range(len(s1), len(s2)):

            # Indices of left char and right char
            lc_idx = ord(s2[left_ptr]) - 97
            rc_idx = ord(s2[right_ptr]) - 97

            #Ugly logic
            if s2[left_ptr] != s2[right_ptr]:
                if s2_map[rc_idx] == s1_map[rc_idx]:
                    matches -= 1
                if s2_map[lc_idx] == s1_map[lc_idx]:
                    matches -= 1
                if s2_map[lc_idx]-1 == s1_map[lc_idx]:
                    matches += 1
                if s2_map[rc_idx]+1 == s1_map[rc_idx]:
                    matches += 1

            s2_map[lc_idx] -= 1
            s2_map[rc_idx] += 1

            left_ptr += 1
            if matches == 26:
                return True

        return False
