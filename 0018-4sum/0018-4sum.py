class Solution:
    def fourSum(self, nums, target):
        nums.sort()  # Sort the array to facilitate the two-pointer technique
        result = []

        for i in range(len(nums) - 3):  # First pointer (a)
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
                continue
            for j in range(i + 1, len(nums) - 2):  # Second pointer (b)
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicates
                    continue
                left, right = j + 1, len(nums) - 1  # Two-pointer approach for (c, d)

                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for the left pointer
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicates for the right pointer
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        # Move both pointers after finding a valid quadruplet
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1  # We need a larger sum, move left pointer
                    else:
                        right -= 1  # We need a smaller sum, move right pointer

        return result

        