# 155. Min Stack

#### Medium

https://leetcode.com/problems/min-stack/

## Solution

If we ignored the pop function, then we could just store the minimum value in one variable. Everytime we pushed a new value, we could check if the new value is the new minimum and update our variable. However, when we add the pop functionality to this, it does not work because what if we pop the minimum value. How would we update the minimum variable in O(1) time?

The solution to this is to utilize a stack that stores the new value AND the minimum value at the point in the stack. Because if we pop a value, then we potentially could be popping the minimum value. So, the new minimum value should be the minimum value stored that existed at the previous node. Therefore, if we push the minimum value variable with the actual new value in a tuple onto our stack, it is clear we can do all operations in O(1) time accurately.
