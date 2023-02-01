#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：leetcode 
@File    ：merge-two-sorted-lists.py
@Author  ：alex
@Date    ：2023/1/31 16:29 
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_list(self, list1, list2):
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.merge_list(list1.next, list2)
            return list1
        else:
            list2.next = self.merge_list(list1, list2.next)
            return list2


if __name__ == '__main__':
    print(Solution().merge([1, 2, 4], [1, 3, 4]))
