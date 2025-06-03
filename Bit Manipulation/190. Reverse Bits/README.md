# 190. Reverse Bits

#### Easy

https://leetcode.com/problems/reverse-bits/description/

## Solution

Since each input integer is gauranteed to be exactly 32 bits, we can actually solve this using a simple for loop.
On each iteration we take the furthest right bit in out input integer by using n & 1. Then, we put this bit into the right most spot of our result variable using the OR operator. Afterwards, we simply shift our result variable to the left once and our n variable to the right once. This reverses the bits because the right bits in our n variable will continously make it to the left of our result variable (reversed). We preform this exactly 32 times because we know our input is 32 bits exactly.
