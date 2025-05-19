# 208. Implement Trie (Prefix Tree)

#### Medium

https://leetcode.com/problems/implement-trie-prefix-tree/description/

## Solution

If we want a efficient startsWith() method, using a simple list or set will NOT be efficient because we would have to iterate the whole list/set each time. Thus, a trie would be much more efficient for this case as each node will represent each character and contain paths for next letters. Therefore, for each method, we will iterate these trie nodes starting at the root. For the insert method, we iterate the tree. When the nodes do not exist for the corresponding character, we simply create it. For the search method, we iterate the tree and return whether all the nodes existed and whether the final/last node was a word node (meaning it was not a prefix to a different word). We do the same thing for the startsWith method but do not return whether the final/last node was a word node.
