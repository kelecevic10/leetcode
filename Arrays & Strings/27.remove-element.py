#

# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

from typing import List

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 
        
        for num in nums:
            if (num != val):
                k += 1
        
        j = k
        for i in range(0, k):
            if (nums[i] == val):
                while (nums[j] == val and j < len(nums)):
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]
                j += 1 
            
        return k


"""
Removes all instances of `val` in-place from the list `nums` and returns the new length `k`.
The solution uses a two-pointer approach:
- The first pointer (`i`) iterates through the first `k` elements of the array, where all elements not equal to `val` should be stored.
- The second pointer (`j`) starts from index `k` and scans the rest of the array.
- For each index `i` in the first part, if `nums[i]` equals `val`, the algorithm advances `j` until it finds an element not equal to `val`, then swaps `nums[i]` and `nums[j]`.
- This ensures that all elements not equal to `val` are moved to the front of the array, and all `val` elements are pushed to the end.
- The function finally returns `k`, the count of elements not equal to `val`.
"""

# @lc code=end

