# 146. LRU Cache

### Medium

https://leetcode.com/problems/lru-cache/description/

## Solution

This problem can be solved with a hashmap and doubly linked list. Its clear we need a hashmap as we must have some sort of O(1) way to index a variety of keys. However, how can this deal with the LRU eviction policy. If too many nodes are put in the cache, how can the hashmap keep track of the LRU key-value pair. The way to get around this is to utilize the doubly linked list. This allows for constant time removals and addition of nodes. Thus, everytime "get" is called, the node in the hashmap should be removed from the list and added to the end of the list to denote it is the most recent key-value pair used. Furthermore, when "put" is called, it should be put in the hashmap and at the end of the list to denote it is the most recent key-value pair used. Now evictions are easy to handle. Any time the amount of nodes in the hashmap exceeds the capacity, the node furthest left/at the head can be removed from the list AND hashmap.