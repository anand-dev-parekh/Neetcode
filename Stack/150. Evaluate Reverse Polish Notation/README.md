# 150. Evaluate Reverse Polish Notation

#### Medium

https://leetcode.com/problems/evaluate-reverse-polish-notation/

## Solution

To solve this question, we can use a stack to implement reverse polish notation. As we iterate through the the input array we will face two cases.

Case 1: integer character

If encounter a integer character, we should push it to the top of our stack. This way, it will be the value first in line for the next operation.

Case 2: operation character

If we have a operation character, we must then pop the two most recent values on the stack. We can then preform the operation, and push the result back onto the stack.

This exactly implements reverse polish notation as it preforms each operation on the two most recent values, and updates the stack with the result.
