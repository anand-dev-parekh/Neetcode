class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> dict = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++){
            if (dict.containsKey(target - nums[i])){
                return new int[]{i, dict.get(target - nums[i])};
            }
            dict.put(nums[i], i);
        }
        return new int[]{0, 0};
    }
}
