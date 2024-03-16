# 238. Product of Array Except Self

#### Medium

https://leetcode.com/problems/product-of-array-except-self/description/

## Solution

The naive idea is to take the product of the whole array. And the returned array indices would be set as such, ans[i] = total_product // nums[i], which is a O(N) process. However, this fails when introduced with cases of 0. Thus, to solve this question we will divide this question into three cases.

Case 1: no Zeroes

If there are no zeroes, we can use the idea stated above, which is to obtain the total product. And then set each array in the ans array equal to total_product // nums[i].

Case 2: 1 Zero

If there is only one zero, then at all points but the zero the answer array should be set to zero, since anything multiplied by 0 == 0. However, we should also calculate the total_product excluding the zero, to store it in the answer array, because if we exclude the one and ONLY zero from the total product calculation we will get a total_product >= 1. So, we must store this in the index of answer where nums[i] == 0.

Case 3: >= 2 Zeroes

If there are more than 2 zeroes, then at any given index there will be another 0 in the array. This means the total product will be 0 for every single point in the answer array.
