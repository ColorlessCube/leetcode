#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：leetcode 
@File    ：3sum-closest.py
@Author  ：alex
@Date    ：2022/12/12 11:33 
"""

# URL: https://leetcode.cn/problems/3sum-closest/
from typing import List


class MySolution:
    def three_sum_closest(self, nums: List[int], target: int) -> int:
        res = 0
        if len(nums) <= 3:
            for num in nums:
                res += num
        i, j, k = 0, 1, 2
        for ntx in range(3, len(nums)):
            i, j, k = self.compute(i, j, k, ntx, nums, target)
            res = nums[i] + nums[j] + nums[k]
            if res == target:
                break
        return res

    def compute(self, i, j, k, ntx, nums, target):
        sum_now = abs(target - (nums[i] + nums[j] + nums[k]))
        sum_i = abs(target - (nums[j] + nums[k] + nums[ntx]))
        sum_j = abs(target - (nums[i] + nums[k] + nums[ntx]))
        sum_k = abs(target - (nums[i] + nums[j] + nums[ntx]))
        min_diff = min(sum_i, sum_j, sum_k, sum_now)
        if min_diff == sum_now:
            return i, j, k
        elif min_diff == sum_i:
            return j, k, ntx
        elif min_diff == sum_j:
            return i, k, ntx
        else:
            return i, j, ntx


class Solution:
    def three_sum_closest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = 10 ** 7

        # 根据差值的绝对值来更新答案
        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur

        # 枚举 a
        for i in range(n):
            # 保证和上一次枚举的元素不相等
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 使用双指针枚举 b 和 c
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                # 如果和为 target 直接返回答案
                if s == target:
                    return target
                update(s)
                if s > target:
                    # 如果和大于 target，移动 c 对应的指针
                    k0 = k - 1
                    # 移动到下一个不相等的元素
                    while j < k0 and nums[k0] == nums[k]:
                        k0 -= 1
                    k = k0
                else:
                    # 如果和小于 target，移动 b 对应的指针
                    j0 = j + 1
                    # 移动到下一个不相等的元素
                    while j0 < k and nums[j0] == nums[j]:
                        j0 += 1
                    j = j0

        return best


if __name__ == '__main__':
    solution = Solution()
    result = solution.three_sum_closest(
        [321, 413, 82, 812, -646, -858, 729, 609, -339, 483, -323, -399, -82, -455, 18, 661, 890, -328, -311, 520, -865,
         -174, 55, 685, -636, 462, -172, -696, -296, -832, 766, -808, -763, 853, 482, 411, 703, 655, -793, -121, -726,
         105, -966, -471, 612, 551, -257, 836, -94, -213, 511, 317, -293, 279, -571, 242, -519, 386, -670, -806, -612,
         -433, -481, 794, 712, 378, -325, -564, 477, 169, 601, 971, -300, -431, -152, 285, -899, 978, -419, 708, 536,
         -816, -335, 284, 384, -922, -941, 633, 934, 497, -351, 62, 392, -493, -44, -400, 646, -912, -864, 835, 713,
         -12, 322, -228, 340, -42, -307, -580, -802, -914, -142, 575, -684, -415, 718, -579, 759, 579, 732, -645, 525,
         114, -880, -603, -699, -101, -738, -887, 327, 192, 747, -614, 393, 97, -569, 160, 782, -69, 235, -598, -116,
         928, -805, -76, -521, 671, 417, 600, -442, 236, 831, 637, -562, 613, -705, -158, -237, -299, 808, -734, 364,
         919, 251, -163, -343, 899]
        , 2218)
    print(result)
