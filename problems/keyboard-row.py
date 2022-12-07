#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：leetcode 
@File    ：keyboard-row.py
@Author  ：alex
@Date    ：2022/12/7 09:21
"""

# URL: https://leetcode.cn/problems/keyboard-row/

from typing import List


class MySolution:
    def find_words(self, words: List[str]) -> List[str]:
        result = []
        lines = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        for word in words:
            if word:
                lower_word = word.lower()
                first_char = lower_word[0]
                line = ''
                for value in lines:
                    if first_char in value:
                        line = value
                        break
                if self.check_word(lower_word, line):
                    result.append(word)
        return result

    def check_word(self, word, line):
        flag = True
        for char in word:
            if char in line:
                continue
            else:
                flag = False
                break
        return flag


# 官方解法
class Solution:
    def find_words(self, words: List[str]) -> List[str]:
        ans = []
        # 按 abcd 的字母顺序获取对应的键盘行号，例如 a 在第一行
        row_idx = "12210111011122000010020202"
        for word in words:
            # ord 计算出 ASCII 码，那么对应字母在 rowIdx 中的 index 就是与 'a' 的相对位置，两者 ASCII 码相减即可
            idx = row_idx[ord(word[0].lower()) - ord('a')]
            # 如果 word 所有的字符都在同一行，那么添加这个 word
            if all(row_idx[ord(ch.lower()) - ord('a')] == idx for ch in word):
                ans.append(word)
        return ans


if __name__ == '__main__':
    words = ["Hello", "Alaska", "Dad", "Peace"]
    solution = MySolution()
    res = solution.find_words(words)
    print(res)
