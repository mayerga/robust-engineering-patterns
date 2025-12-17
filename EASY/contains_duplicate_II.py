"""
CONTAINS DUPLICATE:
Given an integer array nums and an integer k, return true if there are two distinct indices i and j
in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}

        for i, num in enumerate(nums):
            if num in last_seen:
                distancia = i - last_seen[num]
                if distancia <= k:
                    return True
            last_seen[num] = i
        return False

if __name__ == '__main__':
    sol = Solution()
    print(f"Test 1: {sol.containsNearbyDuplicate([1, 2, 3, 1], 3)}")  # True
    print(f"Test 2: {sol.containsNearbyDuplicate([1, 0, 1, 1], 1)}")  # True
    print(f"Test 3: {sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)}")  # False
