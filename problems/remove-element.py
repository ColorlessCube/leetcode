#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：leetcode 
@File    ：remove-element.py
@Author  ：alex
@Date    ：2023/2/1 15:37 
"""
from typing import List


class Solution:
    def remove_element(self, nums: List[int], val: int):
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


if __name__ == '__main__':
    print(Solution().remove_element([3, 2, 2, 3], 3))
