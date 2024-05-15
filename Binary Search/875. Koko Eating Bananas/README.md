# 875. Koko Eating Bananas

### Medium

https://leetcode.com/problems/koko-eating-bananas/

## Solution

### Evaluating k bananas-per-hour eating speed

If we are given some integer k, how do we evaluate if koko can eat all the piles within h hours?

We can do this by looping through the piles and checking how many hours it would take each pile would take using the k banana-per-hour speed. If we ever get to a time that is greater than the h hours, we know it is impossible to finish eating all the bananas with k speed.

### Binary Search for k

The next question is how to we get the minimum k? we could simply start with 0 and increment until we get a k that works. However, this is O(N) and we can do better with binary search (O(logN)). We set our pointers to be 0 and max(piles), because any larger value than max(piles) would be meaningless because there is an hour wait between each pile eating already. After this we simply do a binary search and set left and right pointers based on whether the middle k value in between is feasible or not.

