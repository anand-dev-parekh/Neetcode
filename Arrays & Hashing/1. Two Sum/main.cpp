#include <unordered_map>
#include <vector>

class Solution {
public:
  std::vector<int> twoSum(std::vector<int> &nums, int target) {
    std::unordered_map<int, int> map;
    for (int i = 0; i < nums.size(); i++) {
      int targetNum = target - nums[i];
      if (map.count(targetNum)) {
        return {map[targetNum], i};
      }
      map[nums[i]] = i;
    }
    return {};
  }
};
