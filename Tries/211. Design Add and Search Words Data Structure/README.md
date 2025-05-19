# 211. Design Add and Search Words Data Structure

#### Medium

https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

## Solution

A brute force solution to this problem is simple. We hold a list of words added, and search it every time. But this is not efficient and we can do better by using a trie.
Each node in our trie will represent a lowercase character and it could have 26 possible children.
Whenever we add a new word, we make sure that each node for each character exists otherwise we create one.

In our search method, we simple iterate this tree checking each character has a corresponding node. However, what if one character is a '.', how do we handle this case? To handle this, we make a recursive helper function and return True if any recursive calls are True. Each recursive call will try all of the nodes that exist for the current trienode.
