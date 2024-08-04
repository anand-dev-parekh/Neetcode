# 152. Max Product Subarray

### Medium

https://leetcode.com/problems/maximum-product-subarray/

## Solution

This question is simple. If the numbers in array nums were ALL > 0 then we simply would return the product of the whole array. But adding in the fact that the values could be <= 0 changes things. For example, two negative numbers would make the product positive AND larger, thus we have to take this into account. In order to do this, we must also store a current negative/minimum subarray multiplication score that tracks the minimum current product subarray. That way, when we come across a negative number, we can compare swap values with the current maximum product subarray. We return the max product subarray we came across while iterating through the array.