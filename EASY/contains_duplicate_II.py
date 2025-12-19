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

"""
--- TECHNICAL ANALYSIS ---

Approach: Sliding Window with a Hash Map (Dictionary) for O(1) average time lookups.

1. Logic & Data Structure:
   - I use a Hash Map (dict in Python) to store the most recent index of each value encountered.
   - For each element 'num' at index 'i', we check if it already exists in my 'last_seen' map.
   - If it exists, I calculate the absolute difference (distance) between current 'i' and stored index.
   - Critical Step: I ALWAYS update the map with the current index 'i'. This ensures that for future 
     occurrences, we are comparing against the closest possible previous index, maximizing the 
     probability of meeting the (dist <= k) constraint.

2. Complexities:
   - Time Complexity: O(n) ->I perform a single pass through the array. Dictionary lookups and 
     updates are O(1) on average.
   - Space Complexity: O(min(n, k)) -> In practice, I store at most 'n' elements. However, if I 
     wanted to optimize for memory, I could remove elements from the map that are further than 'k' 
     indices away, keeping the size at 'k'.

3. Key Distinction (Contains Duplicate I vs II):
   - While the first problem only cared about existence (Set), this one requires tracking position (Map) 
     to validate the sliding window constraint 'k'.
"""