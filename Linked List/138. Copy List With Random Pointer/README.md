# 138. Copy List With Random Pointer

### Medium

https://leetcode.com/problems/copy-list-with-random-pointer/

## Solution

The tricky part to this question is the random pointer. This is because if we try simply iterate the list and deep copy the inputted list we will arise with some issues. First, the node could point to something further along in the list. If we create a deep copy of the of the random pointer node, how would be able to get access to it when we reach the node from iterating next in the list. Or, how can we get access to nodes previously created (if random pointer points to something earlier in the list). It would require us to create a duplicate node, but that is NOT a deep copy of the inputted list.

### Hashmap

We can solve these issues my using the almighty hashmap. Every time we iterate next in the list, we should check if the node has previously been found in our hashmap. If it has we should use the value of the hashmap instead of creating another deep copy (we'll see why in a little bit). Otherwise, we can just create a new node with the value given from the input list. 
Then, we should check if the random pointer is in our hashmap. If it is, we should set our node's random pointer value to point to the hashmap value of this random pointer. And, finally we can append our new_node to our deep copy list and add it to the hashmap if it hasn't already been added (same with the random pointer).

This question could've been written better, but the code is pretty self explanatory...