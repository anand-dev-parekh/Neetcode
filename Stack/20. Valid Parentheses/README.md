# 20. Valid Parentheses

#### Easy

https://leetcode.com/problems/valid-parentheses/

## Solution

This question can be simply solved using a stack. For every opening bracket (, {,[ there must be a corresponding closing bracket AFTER the opening bracket. So, flipping that statement around, whenever we hit a closing bracket, that means there MUST have been a opening bracket we have seen previously.

For example:
We will remove each pair inner to outer

({()}[]) -> ({}[]) -> ([]) -> () ->

We can mimick this behaviour using a stack. So, if we iterate all the characters, everytime we hit a opening bracket we will add it to our stack. Then, when we hit a closing bracket, from our statement above, there MUST be the corresponding opening bracket at the top of the stack. So, we can pop it off and return false if they do not correspond. At the end, if the stack's length is 0, that means it was valid since every opening bracket found a corresponding closing bracket and we can return true!
