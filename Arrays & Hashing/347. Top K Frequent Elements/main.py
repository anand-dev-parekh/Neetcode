class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
            SOL: time complexity: O(Nlogn), space: O(N)
                1. iterate nums -> get dict[num] = freq

                2. get array of tuple (num, freq)
                3. sort (array from lambda freq)

                4. return k elements on right side arr
        """

        # Step 1, get num_freq hashmap
        num_freq = {}
        for num in nums:
            if num in num_freq:
                num_freq[num] += 1
            else:
                num_freq[num] = 1

        # Step 2, get array of tuple
        num_freq_arr = []
        for num in num_freq.keys():
            num_freq_arr.append((num, num_freq[num]))

        #Step 3, Sort by freq of tuple
        num_freq_arr.sort(key=lambda x: x[1])

        #Step 4, Return elements on right side of num_freq arr
        ans = []
        for i in range(len(num_freq_arr)-k, len(num_freq_arr)):
            ans.append(num_freq_arr[i][0])
        return ans
