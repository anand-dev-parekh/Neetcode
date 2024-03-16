# 217. Contains Duplicate

#### Easy

https://leetcode.com/problems/contains-duplicate/

#### Solution

This question can be solved by using a hash set. So, iterating through all the elements and checking if the element exists already in the hash set. If it does exist in the hashset that means we have a duplicate and we can return false. Otherwise, we should add the element to the hashset indicating that the current element is in the array, so if it appears again we will return false. If we are able to iterate all elements then we can return true that there were no duplicates!
