# 136. Single Number

#### Easy

https://leetcode.com/problems/single-number/

## Solution

If you XOR the same number: num ^ num, it will always be equal to 0. This is intuitive as they both will have the same binary representation, thus all the bits will be set to 0 after the XOR operation. In our question, every number will appear twice except for one. We also know XOR is an associative operation. If we XOR every number with eachother, then the final result with be the number that appears only once. This is because every other duplicate number would negated eachothers changes, except for the number that appears once.
