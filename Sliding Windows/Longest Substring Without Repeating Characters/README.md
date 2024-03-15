# 3. Longest Substring Without Repeating Characters

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

## Solution

A simple solution to this is to have a hashmap or array of length 26 that points each character to their most recent index found. We will use a sliding window, so continously increment the right pointer while each new character does not exist in the map. However, if the new character already exists in the map, we must move the left pointer to map[new character] + 1. This is because it is impossible to have any substring with unique characters when there are two characters that are the same. So, we can ignore all substrings that have both by moving the left pointer over.

To solve it finally, we can simply return the largest window we found.
