# 17. Letter Combinations of a Phone Number

#### Medium

https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

## Solution

This question follows the same sort of pattern in "39. Combination Sum" and other backtracking problems we have seen so far. Each digit can only map to one letter in a letter combination. However, the letters it can map to vary leading to many combinations given digits from 2-9. A solution to this is to store a hashmap mapping each digit character to the possible letter combinations. We then make recursive calls on our digits, where each level in our tree represents the current digit index. On each recursive call, we loop through these possible letter combinations from our hashmap for the current digit and append it to our current possible letter combination. Then we make another recursive call incrementing our index to the next digit (next level is the next digit). Our base case is when we reach the end of the digits string and append the current possible letter combination to our results list.
