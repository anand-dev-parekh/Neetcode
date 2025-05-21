# 40. Combination Sum II

#### Medium

https://leetcode.com/problems/combination-sum-ii/description/

## Solution

When comparing this question to "39. Combination Sum", there are two key differences to take into account.

1. There are now duplicate numbers in candidates.
2. Each number in candidates can only be used once.

So, how can we keep track of duplicates now and avoid using many instances of the same number? Candidates is not made up of unique elements so our algorithm previously would not work.

For #2, in each recursive call, rather than iterating all indices inclusive from start_i to len(candidates), we would do start_i+1 to len(candidates). This avoids the problem of using each number more than once.

For #1, we could maybe use some data structure to track if we have seen this number before. However, the candidates array is max length of 100, so running a sort() on it would be very quick. Now, since all numbers are sorted, we know where duplicate combinations would be. In each recursive call, we can prevent this by making sure we don't make another recursive call on a number that we have seen before. We can track this by simply comparing each number to the number before it as the array is sorted (if the two numbers are equal then we have seen it). Thus, this will prevent duplicates from coming and get us all combination sums.
