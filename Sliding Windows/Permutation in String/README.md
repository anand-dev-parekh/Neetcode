# 567. Permutation in String

https://leetcode.com/problems/permutation-in-string/description/

## Solution

#### O(26\*N) Solution

In order for s2 to contain some permutation of s1, the size of said permutation must be equal and the map representations of the frequencies of each character in s1 and the s2 substring must be equal. Therefore, we can simply iterate all substrings of size len(s1) and compare if the maps are equal. However, this would be a O(26 \* N) time which is still O(N), but we can slightly optimize this so it is just O(N).

#### O(N) Solution

To remove the computation of comparing the maps every iteration, we can store a integer variable called matches. It stores how many frequencies the two maps agree upon, so if matches == 26, then they are permutations of eachother. Knowing this, we can update the maps and matches everytime we move our left and right pointer over one, rather than iterating 26 times to check if the maps are equal.
