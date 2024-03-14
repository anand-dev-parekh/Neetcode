# 424. Longest Repeating Character Replacement

https://leetcode.com/problems/longest-repeating-character-replacement/

## Solution

#### Evaluating a single subsequence

How can we evaluate one subsequene? For example, ABABAA with k = 2. To do this we can use a map of the frequencies:  
map = {  
A: 4  
B: 2  
}  
  
Since we know the size of the window to be 6, we only care about how many characters there are that are NOT the most frequent character. In other words, we want to replace all other characters in the subsequence with the most frequent character. We can calculate how many replacements must occur by simply taking the length - frequency of most frequent character (6-4 in our example). Since 2 <= 2 this subsequence is valid!

#### Adding a sliding window!

Now if we use a sliding window approach so two pointers, we can use above to evaluate the subsequence. And if the said subseuence is valid, then we can move the right pointer over 1 expanding the window. However, given the case that is not valid, we must shift the left pointer over once. It is only shifted once and does not have to be until the sequence is valid because we are maximizing the window length. So continously shifting/moving it to the right would just make a smaller window than the valid one we just saw, which we are not interested in.
