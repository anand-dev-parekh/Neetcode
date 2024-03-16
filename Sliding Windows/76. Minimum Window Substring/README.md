# 76. Minimum Window Substring

#### Hard

https://leetcode.com/problems/minimum-window-substring/description/

## Solution

This question can be solved using a similiar pattern to 567. Permutation in String. We can turn the characters we are looking for in t into a character frequency map.

#### Evaluating a single substring

If we have a substring "ADOBEC" and we want to know if t="ABC" is valid for such substring, how we would solve it? The frequency map for t looks like something like this:

t_map = {  
A: 1,  
B: 1,  
C: 1  
}  

In order for the substring "ADOBEC" to be valid, we have to make sure all the frequencies in the substrings character:frequency map are >= the frequencies in t_map.

#### Sliding Window!

Now that we have an idea on how to evaluate a single substring, we can add a sliding window to find the minimum window that is valid for the t_map. The idea is to keep track of the windows frequency map as you check windows. So if we have two pointers keeping track of the window, we must iterate the right pointer until the substring is valid. Then we can continously iterate the left pointer until our window is no longer valid. We can repeat this operation until the right pointer reaches the end of string s and return the minimum valid window we found.

Why does this work?
Rather than looking at every single substring, we only look for substrings that are valid. Then we try to minimize the actual size of the substring by shifting the left pointer. This results in O(N) time complexity algorithm that will be able to find the minimum window.

#### Slight Optimization to Validating Substring

Currently, to check if a substring is valid, we iterate both maps and make sure the window map's frequencies are >= the t_map frequencies. To remove this operation, we can store variables called goal_matches and cur_matches where when == the substring is valid, and when != the substring is NOT valid. The idea behind keeping these variables accurate is that whenever we add or remove a character from our window, we compare the frequencies to t_map and increment, decrement, or no change the cur_matches variable.
