# 268. Missing Number

#### Easy

https://leetcode.com/problems/missing-number/

## Solution

For this question, we know the range of the numbers is strictly [0, n] and that array nums is of size n. Therefore, exactly one number is missing from array nums in the range [0, n]. In "136. Single Number" we stated that the XOR operation is associative and num ^ num will always be 0. We can use this exact property again in this question.
Every number in nums will also be in the range of [0, n] EXCEPT for the one missing number. Thus, if we XOR each number with the index (representing the range [0, n]), the duplicate numbers will eliminate each other. This will reveal the one missing number because the corresponding value in nums array does not exist.
