class Solution:
    def countingSort(self, nums: List[int]) -> None:
        freq_map = {}
        minValue = min(nums)
        maxValue = max(nums)

        # Build the frequency map
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        # Sort the array using the frequency map
        idx = 0
        for num in range(minValue, maxValue + 1):
            while freq_map.get(num, 0) > 0:
                nums[idx] = num
                freq_map[num] -= 1
                idx += 1

    def sortArray(self, nums: List[int]) -> List[int]:
        self.countingSort(nums)
        return nums

# Example usage:
solution = Solution()
nums = [4, 2, -3, 3, 1, -2, 4, 2]
sorted_nums = solution.sortArray(nums)
print(sorted_nums)
