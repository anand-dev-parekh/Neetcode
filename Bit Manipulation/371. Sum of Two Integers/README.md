# 371. Sum of Two Integers

#### Medium

https://leetcode.com/problems/sum-of-two-integers/

## Solution

Given two sequences of bits, if we simply took the xor between them, it would essentially be an addition IF there were no 1's aligned in both sequences (would cause carry). Example:

010       011
101       010
---       ---
111       101

In the first example, we never have to carry in our addition, and the + operator is simply the same as an XOR.
In the second example, we need to carry for the 2nd position and the + operator is not equivalent to a XOR.

Thus, how do we account for the carry? Well, we can do this by preforming and storing both a XOR and AND operation on the two integers. The XOR operation will get the addition without any carry values added. The AND value will tell us where there needs to be a carry, of which we shift it left once to represent where the one bit should be. Now, we can add the two results from these and continously do this until the carry is 0.
