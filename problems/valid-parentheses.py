#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：leetcode 
@File    ：valid-parentheses.py
@Author  ：alex
@Date    ：2023/1/31 15:43 
"""


# https://leetcode.cn/problems/valid-parentheses/

class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        left = ['(', '[', '{']
        right = [')', ']', '}']
        for item in s:
            if item in left:
                stack.append(item)
            elif item in right:
                if len(stack) == 0 or stack.pop() != left[right.index(item)]:
                    return False
        if len(stack) != 0:
            return False
        return True


if __name__ == '__main__':
    print(Solution().is_valid('(]'))
