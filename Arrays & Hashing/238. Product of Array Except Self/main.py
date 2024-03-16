class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
            if >= 2 zeroes in nums: Case 1
                always arr of 0's

            if 1 zero: Case 2
                0's except case of the zero

            else 0 zeroes: Case 3
                val is equal to total product/ cur val
        """
        #Get amt of zeroes in nums and index of zero
        zero_cnt = 0
        index = -1
        for i, num in enumerate(nums):
            if num == 0:
                index = i
                zero_cnt += 1

        ans = [0] * len(nums)

        # more than 2 zeroes
        if zero_cnt >= 2:
            return ans

        # only 1 zero
        if zero_cnt == 1:
            nums[index] = 1
            ans[index] = 1
            for i, x in enumerate(nums):
                ans[index] *= nums[i]
            return ans

        # Case 3
        total_product = 1
        for x in nums:
            total_product *= x

        for i in range(len(ans)):
            ans[i] = total_product // nums[i]
        return ans
