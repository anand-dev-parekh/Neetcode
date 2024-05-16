# 2. Add Two Numbers

### Medium

https://leetcode.com/problems/add-two-numbers/description/

## Solution

We can solve this question the same way we solve addition by hand. Add the corresponding digiti numbers and record the carry for the next addition digit addition. Now, instead of writing down the addition, we create a ListNode and record the carry in a local variable. This solution is pretty simple, however, implementing can be a little tough due to some edge cases such as one list being greater in size than the other, the carry going beyond both lists sizes, returning the head of the calculation. However, all of these issues are a culumination of questions seen before or can be solved with very little change.