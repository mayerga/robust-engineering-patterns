"""
Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3,4,1]
    print(sol.containsDuplicate(nums))

    nums2 = [1,2,3,4]
    print(sol.containsDuplicate(nums2))

"""
--- TECHNICAL ANALYSIS ---

Approach: Using a Hash Set to track seen elements for O(1) average time complexity lookups.

1. Set vs List Difference:
   - List: Searching (x in list) takes O(n) because it checks element by element.
   - Set: Searching (x in set) takes O(1) on average because it uses a Hash Table to jump 
     directly to the memory location.

2. Complexities:
   - Time Complexity: O(n) -> We iterate through the array once. Each lookup/insertion is O(1).
   - Space Complexity: O(n) -> In the worst case (all unique elements), the set grows linearly with input size.
"""