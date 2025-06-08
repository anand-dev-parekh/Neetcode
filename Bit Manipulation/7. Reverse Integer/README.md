# 7. Reverse Integer

#### Medium

https://leetcode.com/problems/reverse-integer/

## Solution

The first thing to figure out in this quesiton is how can you get the decimal digits from x. This is intuitive that we can use the % 10 operator to extract each digit individually, and then set x to be // 10. We do this while x is != 0. Now, how do we take these extracted digits and put them in reverse? We can do this by continously multiplying the res variable by 10 and adding the right most digit in the original number. This will successfuly shift each right digit to the left in our res variable.
