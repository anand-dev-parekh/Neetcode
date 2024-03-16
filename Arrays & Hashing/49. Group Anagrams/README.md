# 49. Group Anagrams

#### Medium

https://leetcode.com/problems/group-anagrams/

## Solution

This question can be solved by using a hasmap<string:array> where all keys in the map are unique anagrams. To maintain this condition, as we iterate through all the strings in the array, we will sort each string. If two strings are anagrams of eachother, then the sorted versions of the strings are identical. Therefore, we can append all strings into there retrospective array in the map and return a list of all values (string arrays) from the map.
