"""
Palindrome Number:


Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-231 <= x <= 231 - 1
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        s = str(x)

        return s == s[::-1]

if __name__ == '__main__':
    sol = Solution()
    print(f"Test 1 (121): {sol.isPalindrome(121)}")
    print(f"Test 2 (-121): {sol.isPalindrome(-121)}")
    print(f"Test 3 (10): {sol.isPalindrome(10)}")

"""
--- TECHNICAL ANALYSIS ---

Approach: String conversion and slicing for reversal comparison.

1. Logic:
   - First, I handle the negative number edge case. Any negative number is 
     not a palindrome because the '-' sign appears at the end when reversed.
   - I convert the integer to a string to leverage Python's slicing capabilities.
   - I use the syntax [::-1] to create a reversed copy of the string and 
     compare it with the original.

2. Complexities:
   - Time Complexity: O(n) -> Where n is the number of digits in the integer.
   - Space Complexity: O(n) -> I create a string representation of the number.

3. Optimization Note:
   - While this is readable, I could also solve it mathematically by 
     reversing half of the number to achieve O(1) extra space.
"""