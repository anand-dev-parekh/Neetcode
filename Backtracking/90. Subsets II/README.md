# 90. Subsets II

https://leetcode.com/problems/subsets-ii/

## Solution

In "78. Subsets", our array was made up of completely unique elements. So, we could start at index 0, and make a 2 recursive calls: add current index to subset array or skip over it. And the base case would be when you make it to the end of the array. However, if we were to apply this algorithm to our current question, it would fail. The nums list is NOT made up of unique numbers. So, our recursive calls could possibly add the same combination of numbers to our results array because they are different indices, which is wrong because we only want unique combinations.

One way to avoid counting duplicates is use a recursive level approach like how we did in the Combination Sum questions LC #39 + #40. On each level, we scan through the remaining elements in the array and choose whether to make a recursive call or not to avoid duplicates. And this criteria is actually the same as "40. Combination Sum II". We sort the original nums list. We can track duplicates by simply comparing each number to the number before it as the array is sorted (if the two numbers are equal then we have seen it). If it is a duplicate number, then we will not make a recursive call as one of the previous branches would have added the specific combination/subset.
