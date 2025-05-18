# 22. Generate Parentheses

#### Medium

https://leetcode.com/problems/generate-parentheses/

## Solution

This question can be solved recursively. However, our recursive calls are not so simple. Not every permutation of '(' and ')' of length 2n will be valid. There are two criteria that must stay true to this.

1. The amount of '(' characters should equal amount of ')' characters. So, both have n characters of each.

2. There should never be a ')' character without a corresponding '(' character before it.

We can start solving this question with out base case which would simply be when our string is length of 2n. However, how can we know that this string will be valid. We do this by only making recursive calls that are valid and follow our criteria above. If criteria #1 is valid, we will add '(' to our string and increment the left count variable (tracks how many '(' characters). If criteria #2 is valid, we will add ')' to our string and increment the right count variable.
