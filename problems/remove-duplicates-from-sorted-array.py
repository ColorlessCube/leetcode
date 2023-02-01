#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：leetcode 
@File    ：remove-duplicates-from-sorted-array.py
@Author  ：alex
@Date    ：2023/2/1 15:13 
"""
from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]):
        if not nums:
            return 0
        fast = slow = 1
        while fast < len(nums):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


if __name__ == '__main__':
    print(Solution().remove_duplicates(nums=[1, 1, 2]))
