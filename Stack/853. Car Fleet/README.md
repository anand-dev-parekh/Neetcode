# 853. Car Fleet

#### Medium

https://leetcode.com/problems/car-fleet/

## Solution

When first approaching this problem, you may think that a simulation could solve this problem.
Such as, for each iteration, every value in the position array will be added their corresponding speed value until every car has reached the target.
However, this is very slow if any of the cars speed happen to be 1.
Thus, maybe we can calculate the time it takes using a simple calculation like (target - pos) / speed.
How will we know which cars overlapped and joined fleets and which were independent?


An important note is that given an arbitary car, it can only be limited by cars that start in front of it.
Thus, we can sort our position and speed array based upon the starting position.
Now, starting from the largest position, we loop through the cars and calculate the time taken.
IF any of the times is faster or equal to the slowest time that has been encountered, then it combines with one of the fleets ahead.
Otherwise, it is slower than all of the cars that start before it and we should increment our fleet count.
