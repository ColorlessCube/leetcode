#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：leetcode 
@File    ：search-insert-position.py
@Author  ：alex
@Date    ：2023/2/1 16:36 
"""
from typing import List


class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            center = int((left + right) / 2)
            if nums[center] < target:
                left = center + 1
            elif nums[center] > target:
                right = center
            else:
                return center
        return right


if __name__ == '__main__':
    print(Solution().search_insert(nums=[], target=2))
